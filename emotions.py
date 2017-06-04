# https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/

########### Python 2.7 #############
#import httplib, urllib, requests
import requests
import io
import cv2
import numpy
import json
from collections import namedtuple

# Emotions
# neutral
# contempt
# disgust
# anger
# surprise
# fear
# happiness
# anger

filename = 'images/angry.jpg'


headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'aec19de023c343dd8ab6e137b5788063',
}

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Faces = namedtuple('faces', 'scores')

params = ''
responseJson = ''
strongestEmotion = None


def detectFace(img):
    buff = numpy.fromstring(img, dtype=numpy.uint8)
    image = cv2.imdecode(buff, 1)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    print "Found "+str(len(faces))+" face(s)"
    return faces


def getEmotion(img):
    try:
        response = requests.post(url='https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize',
                        data=img,
                        headers=headers)
        s= response.status_code
        return response.text
    except Exception as e:
        print(e)
        return None


def getStrongestEmotion(emotionJson):
    strongestEmotionValue = 0
    StrongestEmotionName = ''

    parsed = json.loads(emotionJson)
    # print(json.dumps(parsed, indent=4, sort_keys=True))

    for x in parsed:
        s = x['scores']
        for i in s:
            v = s.get(i,{})
            if v > strongestEmotionValue:
                strongestEmotionValue = v
                StrongestEmotionName = i
    
    # print(strongestEmotionValue)
    # print(StrongestEmotionName)

    return StrongestEmotionName


img  = open(filename, 'rb').read()

facesDetected = detectFace(img)

if len(facesDetected) > 0:
    responseJson = getEmotion(img)


    if not responseJson is None:
        strongestEmotion = getStrongestEmotion(responseJson)
        print(strongestEmotion)





