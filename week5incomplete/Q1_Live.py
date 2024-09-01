import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lower_black = np.array([0, 0, 0], dtype=np.uint8)
upper_black = np.array([180, 255, 30], dtype=np.uint8)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_frame, lower_black, upper_black)

    black_background = np.zeros_like(frame)
    black_background[mask > 0] = [255, 255, 255]

    cv2.imshow('Original Frame', frame)

    cv2.imshow('Black Detected as White', black_background)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()
