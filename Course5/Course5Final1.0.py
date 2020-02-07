import zipfile
import PIL
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np








def main():
    # loading the face detection classifier
    face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
    # Creates the data structure to be used in this program
    data_structure = []
    data_strucutre = append_images(data_structure)
    display(data_structure[0]['image'])
    #pre_process_image(data_structure)
    #process_boxes(data_structure)
    #process_text(data_structure)
    #process_faces(data_structure)
    #face_return(data_structure)

def append_images(data_structure):
    with zipfile.ZipFile('small_img.zip', 'r') as f:   #Open the Archive
         for name in f.namelist():  #For each file in the archive
                print("Opening " + name)
                with f.open(name) as imageFile:  #Open the file
                    print("    " +name + " is set to img")
                    img = Image.open(imageFile)  #Set the active image to the file
                    testDictionary = {
                        "image" : img.copy(),
                        "boxes" : [],
                        "text" : [],
                    }

                    data_structure.append(testDictionary)
    return data_structure


main()

# the rest is up to you!

#Read the zipFile
#archive = zipfile.ZipFile('readonly/small_img.zip', 'r')
#for file in archive:
#    img = Image.open(archive.read(file))
#    display(img)
#def append_images():
#    with zipfile.ZipFile('readonly/small_img.zip', 'r') as f:
#         for name in f.namelist():
#                print("Opening " + name)
#                with f.open(name) as imageFile:
#                    print("    " +name + " is set to img")
#                   img = Image.open(imageFile)
#                    testDictionary = {
#                        "image" : img.copy(),
#                        "boxes" : [],
#                        "text" : [],
#                    }
#
#                    data_structure.append(testDictionary)
 #
 #
 #
 #
#append_images()
#preProcess Images()


#Better logic for first part:
    #Create an individual dictionary instance and then append it the global structure



#Working Logic
#Create the dictionaries, add the images, append the dictionary to the global structure
#PreProcess the Image for the boxes, append the boxes to the boxes section
#Process the boxes.   For each box append the text to the test list
#
