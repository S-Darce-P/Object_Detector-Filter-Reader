#202136139 박세호
# An open CV that detects a particular object form a list of objects.
# Shows the quantity of objects and image of the objects being detected.
import cv2
import numpy as np

# Declaration of functions for convenience
def detect_objects():
    # Read image
    img = cv2.imread("./image/horse.jpg")
    height, width, channel = img.shape
    print('original image shape', height, width, channel)

    # Get blob from image
    blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
    print('blob shape:', blob.shape)

    # Read coco object names
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    # Load pre-trained yolo model from configuration and weight files
    net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)

    # Set output layers
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    print(output_layers)

    # Objects
    net.setInput(blob)
    outs = net.forward(output_layers)
    print('shape of the first output:', outs[0].shape)
    print(outs[0][0, :5])

    # Get bounding boxes and confidence scores
    class_ids = []
    confidence_scores = []
    boxes = []

    for out in outs: # For each object
        for detection in out: # For each bounding box
            scores = detection[5:] # Scores for all classes
            class_id = np.argmax(scores) # Class id with max score
            confidence = scores[class_id] # Max score

            if confidence > 0.5:
                # Bounding box coordinates
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle cordinates
                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x, y, w, h])
                confidence_scores.append(float(confidence))
                class_ids.append(class_id)

    # Show the types of objects
    print('number of detected objects =', len(boxes))

    # Non maximum suppression
    indices = cv2.dnn.NMSBoxes(boxes, confidence_scores, 0.5, 0.4)
    print('number of final objects =', len(indices))

    # Draw bounding boxes with labels on image
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # Show the image
    cv2.imshow("Image", img)
    print(classes)
    cv2.waitKey()

    # Type the object that you want to detect
    obj = input("Enter the object that you want to detect: ")
    quantity = 0 # Quantity of detected objects

    for i in range(len(boxes)):
        if i in indices:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])

            # Print detected objects
            if label == obj:
                print(f'class {label} detected at {x}, {y}, {w}, {h}')
                color = colors[i]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                quantity += 1
            
            # Print not detected objects
            else:
                print('%s is not detected' %label)

    # Print Quantity of the detected objects
    print('Quantity of the detected objects: ', quantity)
    cv2.imshow('Objects', img) # Show detected image
    cv2.waitKey()
    cv2.destroyAllWindows()

detect_objects()