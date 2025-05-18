#Basic testing of getting camera feed and doing something with it. Using Laptop camera to start
#REFERENCE - https://www.geeksforgeeks.org/line-detection-python-opencv-houghline-method/ & google AI gave me an example 
# picam stuff https://pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

# import the necessary packages
from picamera2 import Picamera2


import cv2
import numpy as np

# Open the default camera, does this work for default picam? Not sure 
# cam = cv2.VideoCapture(0) #for default webcam on laptop
picam2 = Picamera2() #try this for the picam once picamera is imported and stuff
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)

check = picam2.camera_configuration()['raw']

picam2.start()

while True:
    # Read a frame from the camera. Frame is the actual image as an array. The stuff below manipulates it 
    ret, frame = picam2.capture_array("raw").view(np.uint16)

    # If frame reading was not successful, break
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and help edge detection
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform Canny edge detection
    edges = cv2.Canny(blur, 50, 150)

    # Define the region of interest (ROI) - focus on the lower part of the frame
    height, width = edges.shape
    mask = np.zeros_like(edges)
    polygon = np.array([[(0, height * 2/3), (width, height * 2/3), (width, height), (0, height)]], np.int32)
    cv2.fillPoly(mask, polygon, 255)
    masked_edges = cv2.bitwise_and(edges, mask)

    # Apply Hough Line Transform to detect lines
    lines = cv2.HoughLinesP(masked_edges, 1, np.pi/180, 100, minLineLength=50, maxLineGap=10)

    # Draw the detected lines on the original frame
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)




    # Display the resulting frame
    cv2.imshow('Line Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy all windows
cam.release()
cv2.destroyAllWindows()