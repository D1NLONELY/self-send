import cv2
import numpy as np

video_path = "./image_vid_resources/Cat.mp4"

cap = cv2.VideoCapture(video_path)

lower_white = np.array([0, 0, 180], dtype=np.uint8)
upper_white = np.array([180, 55, 255], dtype=np.uint8)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_frame, lower_white, upper_white)

    white_regions = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Original Frame', frame)

    cv2.imshow('White Mask', mask)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
