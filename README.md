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

python object_size.py --image images/example_01.png --width 0.955
```

## **Results:**
The results are pretty decent even though not perfect. This is due the limitations of the image itself as its not perfect top-down view of the objects and some calibrations could have also been done in the camera before clicking the picture.

![Gif 1 of object dimensions](example_01.gif)
![Gif 2 of object dimensions](example_02.gif)


## **The limitations**
1. This technique requires the image to be near perfect top-down view of the objects to calculate the accurate results. Otherwise the dimensions of the objects in the image may be distorted.