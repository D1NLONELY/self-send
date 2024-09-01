import cv2
import numpy as np

# Path to your video file
video_path = "./image_vid_resources/Cat.mp4"

# Create a VideoCapture object
cap = cv2.VideoCapture(video_path)

# NIGGA

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Define the white color range in HSV
lower_white = np.array([0, 0, 180], dtype=np.uint8)
upper_white = np.array([180, 55, 255], dtype=np.uint8)

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame from BGR to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a binary mask where white colors are detected
    mask = cv2.inRange(hsv_frame, lower_white, upper_white)

    # Bitwise-AND mask and original frame to extract white regions
    white_regions = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame
    cv2.imshow('Original Frame', frame)

    # Display the mask
    cv2.imshow('White Mask', mask)


    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()
