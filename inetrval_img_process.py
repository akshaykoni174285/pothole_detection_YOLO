import os

from ultralytics import YOLO
import cv2

# VIDEOS_DIR = os.path.join('.', 'videos')
# make a videos directory in the project 

# video_path = os.path.join(VIDEOS_DIR, 'vid6.mp4') 
# video_path_out = '{}_out.mp4'.format(video_path)

model_path = os.path.join('.', 'runs', 'detect', 'train4', 'weights', 'last.pt')

pothole_count=0
model = YOLO(model_path)  

threshold = 0.5
class_name_dict = {0: 'pothole'}
for i in range(1,6):
    cap = cv2.imread(f'images/Frame_{i}.jpg')
# ret, frame = cap.read()
    # os.chdir('../')
# H, W, _ = frame.shape
# out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))
 
    
    frame = cap
    
    
   


    results = model(frame)[0]
    pothole_count = pothole_count+len(results)
    # print(results.boxes)

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
    

        if score > threshold:
        
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, class_name_dict[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    cv2.imwrite(f'detec_{i}.jpg',frame)


    # ret, frame = cap.read()
print(f"total number of potholes: {pothole_count}")
# print(pothole_count)
# cap.release()
# out.release()
cv2.destroyAllWindows()