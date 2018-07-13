"""
ECE196 Face Recognition Project
Author: Will Chen

Prerequisite: You need to install OpenCV before running this code
The code here is an example of what you can write to print out 'Hello World!'
Now modify this code to process a local image and do the following:
1. Read geisel.jpg
2. Convert color to gray scale
3. Resize to half of its original dimensions
4. Draw a box at the center the image with size 100x100
5. Save image with the name, "geisel-bw-rectangle.jpg" to the local directory
All the above steps should be in one function called process_image()
"""

# TODO: Import OpenCV
import cv2
import numpy as np


# TODO: Edit this function
def process_image():
    return

# Just prints 'Hello World! to screen.
def hello_world():
    print('Hello World!')
    return

# TODO: Call process_image function.
def main():
    name = 'geisel.jpg'
    
    gray = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
    resize = cv2.resize(gray,None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    height, width = resize.shape
    print height, width
    cv2.rectangle(resize,(50,100),(150,33),(255,255,255),3)
    cv2.imshow('re',resize )
    
    cv2.imwrite('jun.jpg', resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
if(__name__ == '__main__'):
    main()
