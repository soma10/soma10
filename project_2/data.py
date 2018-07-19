import cv2
import glob
import imutils

face_cascade = cv2.CascadeClassifier('/home/pi/opencv-2.4.13.4/data/haarcascades/haarcascade_frontalface_default.xml')
print('face cascades set')
images = glob.glob('/home/pi/facerecognition/lee/lee2/*.jpg')
print('file path set')
number=0
#print(images)
for fname in images:
    print('reading image')
    image = cv2.imread(fname,0)
    rotated = imutils.rotate(image,90)
    print('resizing')
    cut = cv2.resize(rotated, (0, 0), fx = 0.25, fy = 0.25)
    print('resize done')
    #cv2.imshow('cut', cut)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #reimage = cv.resize(gray, (
    faces=face_cascade.detectMultiScale(cut,1.3,5)
    for (x,y,w,h) in faces:
        print('cutting face')
        cropped = cut[y:y+h, x:x+w]
        print('crop done')
        cv2.imwrite('/home/pi/facerecognition/images/17/pic/' + str(number) + '.jpg', cropped)
        print('write done')
        number += 1
        