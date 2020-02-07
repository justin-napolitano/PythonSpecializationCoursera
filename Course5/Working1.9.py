import zipfile
from PIL import Image
from PIL import ImageDraw
import pytesseract
import cv2 as cv
import numpy as np
import kraken
from kraken import pageseg
import string
import sys







def append_images(data_structure):
    with zipfile.ZipFile('readonly/images.zip', 'r') as f:   #Open the Archive
         for name in f.namelist():  #For each file in the archive
                with f.open(name) as imageFile:  #Open the file
                    img = Image.open(imageFile)  #Set the active image to the file
                    testDictionary = {
                        "image" : img.copy(),
                        "boxes" : [],
                        "text" : [],
                        "face_boxes" : [],
                        "file_name" : name
                    }

                    data_structure.append(testDictionary)
    return data_structure


def process_text(data_structure):

    for item in data_structure:
        img = item['image']
        item['text'] = pytesseract.image_to_string(img).replace('-\n','')
        #boxes = item['boxes']
    return data_structure


def detect_faces(data_structure):
    face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier('readonly/haarcascade_eye.xml')
    for item in data_structure:
        cv_img = np.array(item['image'])
        cv_img_grey = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY)
        item['face_boxes'] = face_cascade.detectMultiScale(cv_img_grey, 1.30,4)#.tolist()

'''
        for x,y,w,h in faces:
                face_rectangle = np.array(item['image'].crop((x,y,x+w,y+h)))
                gray = cv.cvtColor(face_rectangle, cv.COLOR_BGR2GRAY)
                eyes = eye_cascade.detectMultiScale(gray)
                if eyes != []:
                    item['face_boxes'].append((x,y,w,h))
                    eyes = []
                else:
                    continue
        #show_rectangles(data_structure, i)
'''
    cv.destroyAllWindows()
    return data_structure

def paste_to_contact_sheet(data_structure):
    #Get test word from user
    test_word = None
    whichFile = None
    small_data_structure = data_structure[:4]
    while test_word != 'quityquit':
        test_word  = input("Enter a keyword: " + "\n" + "enter quityquit to quit" + "\n  ")
        whichFile = input("Which file: 'small' or 'large' would you like to search)" + "\n  ")


        if whichFile == 'small':

#        if breaker != len(data_structure):
#            #for each image test to see if test_word is found in the text
            for item in small_data_structure:
                if test_word in item['text']:
                    print("Word found in {}".format(item['file_name']))
                    if item['face_boxes'] == []:
                        print("But there were no faces in that file")
                    else:
                        img = item['image']
                        #Create a contact sheet
                        contact_sheet = Image.new(img.mode, (550,110*int(np.ceil(len(item['face_boxes'])/5))))
                        p = 0
                        q = 0
                        #For each box found in face boxes....
                    #extract the dimensions
                        box = item['face_boxes']
                        for x,y,w,h in box:
                            #set face equal to the face dimensions and crop from the original image
                            face = img.crop((x,y,x+w,y+h)).resize((110,110))
                            face.thumbnail((110,110))
                            #display(face)
                            #paste the face to the contact sheet
                            contact_sheet.paste(face, (p, q))
                            #change x and y to fit the correct spot in the contact sheet
                            if p+110 == contact_sheet.width:
                                p=0
                                q=q+110
                            else:
                                p=p+110

                        display(contact_sheet)

        elif whichFile == 'large':
#        if breaker != len(data_structure):
#            #for each image test to see if test_word is found in the text
            for item in data_structure:
                if test_word in item['text']:
                    print("Word found in {}".format(item['file_name']))
                    if item['face_boxes'] == []:
                        print("But there were no faces in that file")
                    else:
                        img = item['image']
                        #Create a contact sheet
                        contact_sheet = Image.new(img.mode, (550,110*int(np.ceil(len(item['face_boxes'])/5))))
                        p = 0
                        q = 0
                        #For each box found in face boxes....
                    #extract the dimensions
                        box = item['face_boxes']
                        for x,y,w,h in box:
                            #set face equal to the face dimensions and crop from the original image
                            face = img.crop((x,y,x+w,y+h)).resize((110,110))
                            face.thumbnail((110,110))
                            #display(face)
                            #paste the face to the contact sheet
                            contact_sheet.paste(face, (p, q))
                            #change x and y to fit the correct spot in the contact sheet
                            if p+110 == contact_sheet.width:
                                p=0
                                q=q+110
                            else:
                                p=p+110

                        display(contact_sheet)
        else:
            print("Please enter the correct word: small or large")
            continue



            #for box in item['face_boxes']:



def main():
    # loading the face detection classifier
    #face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
    # Creates the data structure to be used in this program
    %mprun
    data_structure = []
    print("Building Data Structure")
    print("  Appending Images to Structure")
    data_structure = append_images(data_structure)
    print(sys.getsizeof(data_structure))
    print("  Mining images for text")
    data_structure = process_text(data_structure)
    print(sys.getsizeof(data_structure))
    print("  Mining images for faces")
    data_structure = detect_faces(data_structure)
    print(sys.getsizeof(data_structure))
    print("The Data Structure is complete")
    print("Get ready to search!")
    paste_to_contact_sheet(data_structure)

main()
