import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import typing as tp

image_path = "./image_vid_resources/Untitled.jpeg"
image = cv.imread(image_path)
cv.namedWindow("image")
cv.imshow("image", image)
cv.waitKey(0)
cv.destroyAllWindows()

grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

tl = 300
th = 854
canny_edges = cv.Canny(grey_image, tl, th)

win_name = "hough"
cv.namedWindow(win_name)
cv.imshow(win_name, canny_edges)
cv.waitKey(0)
cv.destroyAllWindows()

rho = 9
theta = 0.261
threshold = 101

def hough_lines(edges: np.ndarray, threshold: float, min_theta: float, max_theta: float) -> np.ndarray:
    diagonal = np.sqrt(edges.shape[0]**2 + edges.shape[1]**2)
    theta_angles = np.arange(min_theta, max_theta, theta)
    rho_values = np.arange(-diagonal, diagonal, rho)
    num_thetas = len(theta_angles)
    num_rhos = len(rho_values)
    accumulator = np.zeros([num_rhos, num_thetas])

    sins = np.sin(theta_angles)
    coss = np.cos(theta_angles)

    xs, ys = np.where(edges > 0)

    for x, y in zip(xs, ys):
        for t in range(num_thetas):
            current_rho = x * coss[t] + y * sins[t]
            rho_pos = np.argmin(np.abs(current_rho - rho_values))
            accumulator[rho_pos, t] += 1

    lines = np.argwhere(accumulator > threshold)
    rho_lines = rho_values[lines[:, 0]]
    theta_lines = theta_angles[lines[:, 1]]

    return np.vstack([rho_lines, theta_lines]).T

def polar2cartesian(radius: np.ndarray, angle: np.ndarray) -> np.ndarray:
    return radius * np.array([np.sin(angle), np.cos(angle)])

def draw_lines(img: np.ndarray, lines: np.ndarray, color: tp.List[int] = [0, 0, 255], thickness: int = 1) -> tp.Tuple[np.ndarray, np.ndarray]:
    new_image = np.copy(img)
    empty_image = np.zeros(img.shape[:2])

    if len(lines.shape) == 1:
        lines = lines[None, ...]

    for rho, theta in lines:
        x0, y0 = polar2cartesian(rho, theta)
        direction = np.array([y0, -x0])
        pt1 = np.round([x0 + 1000 * direction[0], y0 + 1000 * direction[1]]).astype(int)
        pt2 = np.round([x0 - 1000 * direction[0], y0 - 1000 * direction[1]]).astype(int)
        empty_image = cv.line(img=empty_image, pt1=pt1, pt2=pt2, color=255, thickness=thickness)

    mask_lines = empty_image != 0
    new_image[mask_lines] = np.array(color)

    return new_image, mask_lines

lines = hough_lines(canny_edges, threshold, -np.pi/2, np.pi/2)

lines_img, mask = draw_lines(image, lines)
cv.waitKey(0)
cv.destroyAllWindows()