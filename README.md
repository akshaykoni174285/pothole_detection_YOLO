# pothole_detection_YOLO


## Results

<img src="https://i.imgur.com/ITBYDQv.png">
<img src="https://i.imgur.com/imaAFaM.png">
<img src="https://i.imgur.com/QxuPF9r.png">
<img src="https://i.imgur.com/CXZdMe3.png">
<img src="https://i.imgur.com/BYwoAcx.png">
<img src ="https://i.imgur.com/ijm8xag.png">


 1. If you're looking to identify potholes in video footage and subsequently save the video with bounding boxes, you can utilize the 'cap_vid_model_save.py' script. This script is designed to both detect potholes and preserve the video, saving it in the .avi format.
 2. if you want to count the potholes then the cap_img.py will snapshot the pic of pothole every 5 sec for which our drone will be moving in a constant velocity ensuring no duplicasy of potholes from frames and then it will save the pics in a folder which will ready to be processed
 3. then to count and apply bounding boxes on the images taken use interval_img_process.py which will process each image and also track the no of potholes 
<!-- <br/>
<b>Step 6.</b> Manually divide collected images into two folders train and test. So now all folders and annotations should be split between the following two folders. <br/>
\TFODCourse\Tensorflow\workspace\images\train<br />
\TFODCourse\Tensorflow\workspace\images\test
<br/><br/>
<b>Step 7.</b> Begin training process by opening <a href="https://github.com/nicknochnack/TFODCourse/blob/main/2.%20Training%20and%20Detection.ipynb">2. Training and Detection.ipynb</a>, this notebook will walk you through installing Tensorflow Object Detection, making detections, saving and exporting your model. 
<br /><br/>
<b>Step 8.</b> During this process the Notebook will install Tensorflow Object Detection. You should ideally receive a notification indicating that the API has installed successfully at Step 8 with the last line stating OK.   -->

<!-- If not, resolve installation errors by referring to the <a href="https://github.com/nicknochnack/TFODCourse/blob/main/README.md">Error Guide.md</a> in this folder.
<br /> <br/>
<b>Step 9.</b> Once you get to step 6. Train the model, inside of the notebook, you may choose to train the model from within the notebook. I have noticed however that training inside of a separate terminal on a Windows machine you're able to display live loss metrics.  -->

<!-- <br />
<b>Step 10.</b> You can optionally evaluate your model inside of Tensorboard. Once the model has been trained and you have run the evaluation command under Step 7. Navigate to the evaluation folder for your trained model e.g. 
<pre> cd Tensorlfow/workspace/models/my_ssd_mobnet/eval</pre> 
and open Tensorboard with the following command
<pre>tensorboard --logdir=. </pre>
Tensorboard will be accessible through your browser and you will be able to see metrics including mAP - mean Average Precision, and Recall.
<br /> -->
