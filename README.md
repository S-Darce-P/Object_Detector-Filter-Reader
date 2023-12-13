## Object_Detecter-Filter-Reader with OpenCV
### Product Description
**Object Detecter** detects the object that the user is looking for in the given image, and indicates the number of the object

**Object Filter** filters only the objects desired by the user among the detected objects, and indicate the quantity

**Object Reader** detects objects from real-time images through the camera and outputs the names of the detected objects as a voice.

## **Requirements: (with versions i tested on)**
1. python          (3.12.0)  
https://www.python.org/downloads/
2. opencv          (4.8.1)  
% pip install opencv-python
3. numpy           (1.26.2)  
% pip install numpy
4. YOLOv3  
https://pjreddie.com/media/files/yolov3.weights  
https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg  
https://github.com/pjreddie/darknet/blob/master/data/coco.names  
5. pyttsx3  
% pip install pyttsx3

## **Commands to run the product:**
```
**Object_detector.py**
% python Object_detector.py

**Object_filter.py**
% python Object_filter.py

**Object_reader.py**
% python Object_reader.py
```

## **Results:**
The results of the Object_detector/filter are quite accurate and work perfectly without errors.  
The results of the Object_reader shows decent accuracy, but the reader doesn't pronounce well, and the video camera works slowly with a very low frame.

**Object Detector**  
![Object_detector](https://github.com/S-Darce-P/object_detector-filter-reader/assets/142721563/43450448-7bb4-419b-b541-d896094c5b73)

**Object Filter**  
![Object_filter](https://github.com/S-Darce-P/object_detector-filter-reader/assets/142721563/82ba3449-382b-4686-b346-8a32f40634d6)

**Object Reader**
![Object-Reader](https://github.com/S-Darce-P/object_detector-filter-reader/assets/142721563/7976ace7-aba7-4fd5-9954-e3350a17219c)

video with sound  
https://github.com/S-Darce-P/object_detector-filter-reader/assets/142721563/881cf552-afc0-4c47-8e36-ee139456cc73

## **References**
https://docs.opencv.org/master/d6/d0f/group__dnn.html  
https://pjreddie.com/darknet/yolo/  
https://pypi.org/project/pyttsx3/
