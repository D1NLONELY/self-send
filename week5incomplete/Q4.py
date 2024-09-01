import cv2

def main():
    image_path = './image_vid_resources/Untitled.jpeg'
    image = cv2.imread(image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    try:
        threshold_value = int(input("Enter the threshold value (0-255): "))
        if not (0 <= threshold_value <= 255):
            raise ValueError("Threshold value must be between 0 and 255.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    max_value = 255
    _, binary_image = cv2.threshold(gray_image, threshold_value, max_value, cv2.THRESH_BINARY)

    output_path = 'binary_image_global.jpg'
    cv2.imwrite(output_path, binary_image)
    print(f"Binary image saved as {output_path}")
    
    cv2.imshow('Binary Image', binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
