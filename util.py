import numpy as np
import cv2

def get_limits(color):
    c = np.uint8([[color]])  # Convert BGR to HSV
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # Define lower and upper HSV bounds with margin
    lowerLimit = hsvC[0][0] - [10, 100, 100]
    upperLimit = hsvC[0][0] + [10, 255, 255]

    # ✅ Use np.clip to ensure values stay in 0–255 range
    lowerLimit = np.clip(lowerLimit, 0, 255)
    upperLimit = np.clip(upperLimit, 0, 255)

    # Convert to uint8 arrays
    return np.array(lowerLimit, dtype=np.uint8), np.array(upperLimit, dtype=np.uint8)
