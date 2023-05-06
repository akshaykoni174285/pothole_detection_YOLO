import numpy as np
from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import *

cap = cv2.VideoCapture("videos/vid6.mp4")  # For Video

model = YOLO("YOLOv8n.pt")

classNames = ["potholes"]



# Tracking



while True:
    success, img = cap.read()
    
    results = model(img, stream=True)
    

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
            w, h = x2 - x1, y2 - y1

            cvzone.cornerRect(img,(x1,y1,w,h),3)
            
            conf = math.ceil((box.conf[0] * 100)) /100
            
            cls = int(box.cls[0])
            
            cvzone.putTextRect(img,f'{classNames[cls]} {conf}', (max(0,x1),max(35,y1)), scale=1,thickness=1)
            
    cv2.imshow("Image", img)
    # cv2.imshow("ImageRegion", imgRegion)
    cv2.waitKey(1)