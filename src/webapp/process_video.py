import json

import cv2
import numpy as np

import hand_recognize

# import classify

camera = cv2.VideoCapture(0)
i = 0


def frame_process():  # generate frame by frame from camera
    """
    This function is used to read frames from the camera and run the gesture recognition model on them.
    :return: frame bytes from camera augmented by gesture recognition model
    """
    global i
    while True:
        # Capture frame by frame
        success, frame = camera.read()
        if success:
            # Flip the frame vertically
            frame = cv2.flip(frame, 1)

            frame, landmarks, gestures, palm_orientation = hand_recognize.hand_feature_extract(frame, i)
            i = i + 1
            label = f"{gestures[0].category_name} ({np.round(gestures[0].score, decimals=2)}) [{palm_orientation}]" if gestures else ""
            if label != "":
                with open("tmp/video_prediction.json", "r+") as fp:
                    data = json.load(fp)
                    while len(data["labels"]) >= 4:
                        data["labels"].pop(0)
                    data["labels"].append(label)
                    fp.seek(0)
                    fp.truncate()
                    json.dump(data, fp)

            # show the prediction on the frame
            cv2.putText(frame, label, (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2, cv2.LINE_AA)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'  # concat frame one by one and show result
        else:
            break
