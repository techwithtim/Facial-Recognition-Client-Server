import requests
import io
import cv2
import base64 
import numpy as np
from PIL import Image

def string_to_image(base64_string):
    imgdata = base64.b64decode(base64_string)
    return np.array(Image.open(io.BytesIO(imgdata)))


url = 'http://localhost:5000/classify-faces'
my_img = {'image': open('test-image.jpg', 'rb')} # feel free to change the image path here
r = requests.post(url, files=my_img)

img_str = r.json().get("image").split('\'')[1]
img = string_to_image(img_str)

while True:
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
