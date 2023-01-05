from copy import deepcopy
from time import sleep

import cv2
import mediapipe as mp
import numpy as np
from mediapipe.framework.formats import landmark_pb2

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path='gesture_recognizer.task'),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=1,
    min_hand_detection_confidence=0.3,
    min_hand_presence_confidence=0.3,
    min_tracking_confidence=0.3
)

recognizer = GestureRecognizer.create_from_options(options)

# initialize mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils


def hand_feature_extract(frame, timestamp):
    # frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

    result = recognizer.recognize_for_video(mp_image, timestamp)
    landmarks = []
    gestures = None
    normal_vector = []
    palm_orientation = ""
    x, y, _ = frame.shape
    if result.hand_landmarks:
        if result.gestures:
            gestures = result.gestures[0]
            for gesture in gestures:
                if gesture.category_name == 'none':
                    gesture.category_name = '0' # since while training we changed the 0 label to none
        for hands_landmarks in result.hand_landmarks:
            for lm in hands_landmarks:
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy, lm.z])
            # Drawing landmarks on frames
            hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            hand_landmarks_proto.landmark.extend([
                landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in
                hands_landmarks
            ])

            mp_drawing.draw_landmarks(frame, hand_landmarks_proto, mp_hands.HAND_CONNECTIONS)

            points = np.asarray([[hands_landmarks[0].x, hands_landmarks[0].y, hands_landmarks[0].z],
                                 [hands_landmarks[5].x, hands_landmarks[5].y, hands_landmarks[5].z],
                                 [hands_landmarks[17].x, hands_landmarks[17].y, hands_landmarks[17].z]])
            WL = points[1] - points[0]
            WI = points[2] - points[0]
            if result.handedness[0][0].category_name.lower() == 'left':
                normal_vector = np.cross(WI, WL)
            else:
                normal_vector = np.cross(WL, WI)
            normal_vector /= np.linalg.norm(normal_vector)
            normal_vector = np.round(normal_vector, decimals=2)
            # print(normal_vector, "\n")

        k = 0.3
        # palm_orientation = f"({normal_vector[0]}, {normal_vector[1]}, {normal_vector[2]}) "
        index = np.argmax(np.abs(normal_vector))
        if index == 0:
            if normal_vector[0] < -k:
                palm_orientation += "right"
            elif normal_vector[0] > k:
                palm_orientation += "left"
        if index == 1:
            if normal_vector[1] < -k:
                palm_orientation += "down"
            elif normal_vector[1] > k:
                palm_orientation += "up"
        if index == 2:
            if normal_vector[2] < -k:
                palm_orientation += "body"
            elif normal_vector[2] > k:
                palm_orientation += "front"

    return frame, landmarks, gestures, palm_orientation
