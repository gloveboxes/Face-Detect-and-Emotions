#https://github.com/opencv/opencv/tree/master/data/haarcascades
#https://realpython.com/blog/python/face-recognition-with-python/
#https://pythonprogramming.net/raspberry-pi-camera-opencv-face-detection-tutorial/
#https://stackoverflow.com/questions/27069789/the-correct-manner-to-install-opencv-in-raspberrypi-to-use-it-with-python
#https://oscarliang.com/raspberry-pi-face-recognition-opencv/
#sudo apt install python-opencv


import io
import cv2
import numpy


#body = open('faces.jpg', 'rb').read()

# image = cv2.imread("faces.jpg") 

print('starting')



# buff = numpy.fromstring(img, dtype=numpy.uint8)

# image = cv2.imdecode(buff, 1)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

print('loading image')

image = cv2.imread("face.png")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

print('detecting')

faces = face_cascade.detectMultiScale(gray, 1.1, 5)

print "Found "+str(len(faces))+" face(s)"

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

#Save the result image
cv2.imwrite('result.jpg',image)