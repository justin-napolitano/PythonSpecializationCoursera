import zipfile

from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# the rest is up to you!

#Read the zipFile
#archive = zipfile.ZipFile('readonly/small_img.zip', 'r')
#for file in archive:
#    img = Image.open(archive.read(file))
#    display(img)
with zipfile.ZipFile('small_img.zip', 'r') as f:
     for name in f.namelist():
            print("Opening " + name)
            with f.open(name) as imageFile:
                print("    " +name + " is set to img")
                img = Image.open(imageFile)
                display(img)
