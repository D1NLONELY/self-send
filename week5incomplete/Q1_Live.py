import cv2
import numpy as np

# Create a VideoCapture object for the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Define the black color range in HSV
lower_black = np.array([0, 0, 0], dtype=np.uint8)
upper_black = np.array([180, 255, 30], dtype=np.uint8)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame from BGR to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a binary mask where black colors are detected
    mask = cv2.inRange(hsv_frame, lower_black, upper_black)

    # Create a black background
    black_background = np.zeros_like(frame)

    # Convert black regions to white on the black background
    black_background[mask > 0] = [255, 255, 255]

    # Display the original frame
    cv2.imshow('Original Frame', frame)

    # Display the result where black is detected as white and all else is black
    cv2.imshow('Black Detected as White', black_background)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()
