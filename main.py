import numpy as np
import matplotlib
import cv2
from PIL import Image
from util import get_limits

yellow = [0, 255, 255]
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color=yellow)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Fix the typo here
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    if bbox is not None:
      x1, y1, x2, y2 = bbox
      frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
    cv2.imshow('frame', frame)  # Show original frame with box
    cv2.imshow('mask', mask)    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
