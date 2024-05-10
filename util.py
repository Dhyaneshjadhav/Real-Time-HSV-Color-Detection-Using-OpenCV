import numpy as np
import cv2

def get_limits(color):
    # Convert BGR to HSV
    hsv_color = cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_BGR2HSV)
    hue = hsv_color[0][0][0]  # Get the hue value

    # Define hue limits
    lower_hue = (hue - 10) % 180
    upper_hue = (hue + 10) % 180

    # Define lower and upper limits
    lower_limit = np.array([lower_hue, 100, 100], dtype=np.uint8)
    upper_limit = np.array([upper_hue, 255, 255], dtype=np.uint8)

    return lower_limit, upper_limit
