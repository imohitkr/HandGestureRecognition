import cv2
import mediapipe as mp

# initialize mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils


def hand_feature_extract(frame):
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(framergb)
    landmarks = []
    x, y, _ = frame.shape
    if result.multi_hand_landmarks:
        for hands_landmarks in result.multi_hand_landmarks:
            for lm in hands_landmarks.landmark:
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy, lm.z])
            # Drawing landmarks on frames
            mp_drawing.draw_landmarks(frame, hands_landmarks, mp_hands.HAND_CONNECTIONS)

    return frame, landmarks

