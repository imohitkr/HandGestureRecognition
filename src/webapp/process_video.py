import cv2
import hand_recognize

camera = cv2.VideoCapture(0)


def frame_process():  # generate frame by frame from camera
    while True:
        # Capture frame by frame
        success, frame = camera.read()
        if success:
            # Flip the frame vertically
            frame = cv2.flip(frame, 1)

            frame, landmarks = hand_recognize.hand_feature_extract(frame)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'  # concat frame one by one and show result
        else:
            break
