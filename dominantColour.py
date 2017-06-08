# https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv
# http://picamera.readthedocs.io/en/release-1.10/recipes1.html#capturing-in-low-light
# http://rapidtables.com/web/color/RGB_Color.htm

# sudo pip install opencv-python
# sudo pip install picamera
# sudo apt install scipy
# sudo apt install python-opencv



import cv2
import numpy as np
import io
from scipy.stats import itemfreq
import picamera
from time import sleep




stream = io.BytesIO()
camera = picamera.PiCamera()

camera.resolution = (320, 240)
sleep(2)

camera.capture('foo.jpg')
camera.capture(stream, format='jpeg')
stream.seek(0)
image = stream.getvalue()

buff = np.fromstring(image, dtype=np.uint8)
img = cv2.imdecode(buff, 1)


# img = cv2.imread('blue.jpg')


arr = np.float32(img)
pixels = arr.reshape((-1, 3))

n_colors = 4
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, .1)
flags = cv2.KMEANS_RANDOM_CENTERS


_, labels, centroids = cv2.kmeans(pixels, n_colors, criteria, 10, flags)

palette = np.uint8(centroids)
quantized = palette[labels.flatten()]
quantized = quantized.reshape(img.shape)

dominant_color = palette[np.argmax(itemfreq(labels)[:, -1]) - 1]

print(dominant_color)


camera.close()
