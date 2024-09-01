import cv2
import numpy as np

# Define input and output video paths
input_video_path = './image_vid_resources/Cat.mp4'  # Replace with your video file
output_video_path = './image_vid_resources/Cat_K_Means.mp4'  # Output video file path

# Open the video file
cap = cv2.VideoCapture(input_video_path)

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define the codec and create VideoWriter object
out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

# Define K-means parameters
k = 3  # Number of clusters
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)  # Stopping criteria
attempts = 10  # Number of attempts for K-means

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Reshape the frame to a 2D array of pixels
    pixel_values = frame.reshape((-1, 3))
    pixel_values = np.float32(pixel_values)

    # Apply K-means clustering
    _, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, attempts, cv2.KMEANS_RANDOM_CENTERS)

    # Convert centers to 8-bit values
    centers = np.uint8(centers)

    # Map the labels to the cluster centers
    segmented_image = centers[labels.flatten()]

    # Reshape segmented image to the original frame shape
    segmented_image = segmented_image.reshape(frame.shape)

    # Write the frame to the output video file
    out.write(segmented_image)

    # Display the frame with K-means clustering applied
    cv2.imshow('K-means Clustering', segmented_image)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and writer objects and close windows
cap.release()
out.release()
cv2.destroyAllWindows()
