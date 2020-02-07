import zipfile
from PIL import Image
from PIL import ImageDraw
import pytesseract
import cv2 as cv
import numpy as np
import kraken
from kraken import pageseg
import string




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
                        "line_height" : 0,
                        "face_boxes" : []
                    }

                    data_structure.append(testDictionary)
    return data_structure


def display_images(data_structure):
    display(data_structure[0]['image'])


def set_text_boxes(data_structure):
    '''Modifies the passed image to show a series of bounding boxes on an image as run by kraken

    :param img: A PIL.Image object
    :return img: The modified PIL.Image object
    '''
    print("Running set_text_boxes...")
    for item in data_structure:
        print("  loading an item in the dictionary")
        img = item["image"]
    # And grab a drawing object to annotate that image
        drawing_object=ImageDraw.Draw(img)
    # We can create a set of boxes using pageseg.segment
        print("    setting the boxes key now")
        item['boxes']=pageseg.segment(img.convert('1'), black_colseps=True)['boxes']
    # Now lets go through the list of bounding boxes
        for box in item['boxes']:
        # An just draw a nice rectangle
            #print("        Drawing rectangles....")
            drawing_object.rectangle(box, fill = None, outline ='red')
    # And to make it easy, lets return the image object
    return data_structure




def calculate_line_height(data_structure):
    '''Calculates the average height of a line from a given image
    :param img: A PIL.Image object
    :return: The average line height in pixels
    '''
    # Lets get a list of bounding boxes for all images in the data structure
    for item in data_structure:
        img = item['image']
        item['boxes'] = bounding_boxes=pageseg.segment(img.convert('1'))['boxes']


    # Each box is a tuple of (top, left, bottom, right) so the height is just top - bottom
    # So lets just calculate this over the set of all boxes

    for item in data_structure:
        height_accumulator=0
        print("  Setting a line height for an image")
        for box in item['boxes']:

            height_accumulator=height_accumulator+box[3]-box[1]
        # this is a bit tricky, remember that we start counting at the upper left corner in PIL!
    # now lets just return the average height
    # lets change it to the nearest full pixel by making it an integer
        item['line_height'] = int(height_accumulator/len(bounding_boxes))
        print("   Line height has been set")
    print("line heights sucessfully calculated")
    return data_structure

#line_height=calculate_line_height(Image.open("readonly/two_col.png"))
#print(line_height)





# we find a gap? For this, lets just draw a line in the middle of it. Lets create a new function
def draw_sep(img,location):
    '''Draws a line in img in the middle of the gap discovered at location. Note that
    this doesn't draw the line in location, but draws it at the middle of a gap_box
    starting at location.
    :param img: A PIL.Image file
    :param location: A tuple(x,y) which is a pixel location in the image
    '''
    # First lets bring in all of our drawing code

    drawing_object=ImageDraw.Draw(img)
    # next, lets decide what the middle means in terms of coordinates in the image
    x1=location[0]+int(gap_box[2]/2)
    # and our x2 is just the same thing, since this is a one pixel vertical line
    x2=x1
    # our starting y coordinate is just the y coordinate which was passed in, the top of the box
    y1=location[1]
    # but we want our final y coordinate to be the bottom of the box
    y2=y1+gap_box[3]
    drawing_object.rectangle((x1,y1,x2,y2), fill = 'black', outline ='black')
    # and we don't have anything we need to return from this, because we modified the image

def gap_check(img, location, gap_box):
    '''Checks the img in a given (x,y) location to see if it fits the description
    of a gap_box
    :param img: A PIL.Image file
    :param location: A tuple (x,y) which is a pixel location in that image
    :return: True if that fits the definition of a gap_box, otherwise False
    '''

    # Recall that we can get a pixel using the img.getpixel() function. It returns this value
    # as a tuple of integers, one for each color channel. Our tools all work with binarized
    # images (black and white), so we should just get one value. If the value is 0 it's a black
    # pixel, if it's white then the value should be 255
    #
    # We're going to assume that the image is in the correct mode already, e.g. it has been
    # binarized. The algorithm to check our bounding box is fairly easy: we have a single location
    # which is our start and then we want to check all the pixels to the right of that location
    # up to gap_box[2]
    for x in range(location[0], location[0]+gap_box[2]):
        # the height is similar, so lets iterate a y variable to gap_box[3]
        for y in range(location[1], location[1]+gap_box[3]):
            # we want to check if the pixel is white, but only if we are still within the image
            if x < img.width and y < img.height:
                # if the pixel is white we don't do anything, if it's black, we just want to
                # finish and return False
                if img.getpixel((x,y)) != 255:
                    return False
    # If we have managed to walk all through the gap_box without finding any non-white pixels
    # then we can return true -- this is a gap!
    return True


def process_images(data_structure):
    '''Takes in an image of text and adds black vertical bars to break up columns
    :param img: A PIL.Image file
    :return: A modified PIL.Image file
    '''
    # we'll start with a familiar iteration process
    char_width = 25
    for item in data_structure:
        img = item["image"]
        line_height = item['line_height']
        gap_box=(0,0,char_width,line_height*6)
        for x in range(img.width):
            for y in range(img.height):
                # check if there is a gap at this point
                if (gap_check(img, (x,y), gap_box)):
                    # then update image to one which has a separator drawn on it
                    draw_sep(img, (x,y),gap_box)
        # and for good measure we'll return the image we modified
    return data_structure



def binarize(image_to_transform, threshold):
    output_image=image_to_transform.convert("L")
    for x in range(output_image.width):
        for y in range(output_image.height):
            if output_image.getpixel((x,y))< threshold:
                output_image.putpixel( (x,y), 0 )
            else:
                output_image.putpixel( (x,y), 255 )
    return output_image



def process_text(data_structure):
    eng_dict=[]
    with open ("words_alpha.txt", "r") as f:
        data=f.read()
        # now we want to split this into a list based on the new line characters
        eng_dict=data.split("\n")
    for item in data_structure:
        img = item['image']
        str = item['text']
        boxes = item['boxes']
        for box in boxes:
            tmp_img=img.crop(box).resize(new_size, Image.BICUBIC)

            # Now lets iterate through all possible thresholds and look for an english word, printing
            # it out if it exists
            for i in range(150,170):
                # lets binarize and convert this to s tring values
                strng=pytesseract.image_to_string(binarize(tmp_img,i))
                # We want to remove non alphabetical characters, like ([%$]) from the text, here's
                # a short method to do that
                # first, lets convert our string to lower case only
                strng=strng.lower()
                # then lets import the string package - it has a nice list of lower case letters
                # now lets iterate over our string looking at it character by character, putting it in
                # the comaprison text
                comparison=''
                for character in strng:
                    if character in string.ascii_lowercase:
                        comparison=comparison+character
                # finally, lets search for comparison in the dictionary file
                if comparison in eng_dict:
                    # and print it if we find it
                    #print(comparison)
                    #now append the string to string for the entire image...
                    str.append(strng)

def detect_faces(data_structure):
    face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier('readonly/haarcascade_eye.xml')
    i = 0
    for item in data_struture:
        cv_img = cv.imread(item['image'])
        item['face_boxes'] = face_cascade.detectMultiScale(cv_img, 1.25)
        show_rectangles(data_structure, i)
        i+=1
    return data_structure


def show_rects(data_structure, i):
    #Lets read in our gif and convert it
    img = data_structure[i]['image']convert('RGB')
    faces= data_strucutre[i]['face_boxes']
    # Set our drawing context
    drawing=ImageDraw.Draw(img)
    # And plot all of the rectangles in faces
    for x,y,w,h in faces:
        drawing.rectangle((x,y,x+w,y+h), outline="white")
    #Finally lets display this
    display(img)



    #cv_img=cv.imread('msi_recruitment.png')
    #faces = face_cascade.detectMultiScale(cv_img,1.25)
    #cv_img_bin=cv.threshold(img,120,255,cv.THRESH_BINARY)[1]





def main():
    # loading the face detection classifier
    #face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
    # Creates the data structure to be used in this program
    data_structure = []
    print("Saving images to the data structure")
    data_structure = append_images(data_structure)

    #Get line height.

    #print("Calculating line height for each image in data structure")
    #data_structure = calculate_line_height(data_structure)

    #print('Processing the images')
    #process all images

    #data_structure = process_images(data_structure)

    #data_structure = set_text_boxes(data_structure)

    #print('Procesing Text in images')
    #data_structure = process_text(data_strucutre)
     data_strcutre = detect_faces(data_structure)

    '''
    # a quick way to iterate through the keys to see if line_height is setting
    Print("testing line height now")
    i = 0
    for item in data_structure:
        print("The height of image {} is {}".format(i,item["line_height"]))
        i+=1
    '''
    #if this is done correctly i need to then get text and then get faces


    #process_images(data_structure)
    #get_boxes(data_structure)
    #get_faces(data_structure)
    #
    #print("Finding Textboxes and drawing boxes")
    #display_images(data_structure)
    #show_boxes(data_structure)
    #i.show()
    #print("Beginning image Pre Processing")

    #pre_process_image(data_structure)
    #process_boxes(data_structure)
    #process_text(data_structure)
    #process_faces(data_structure)
    #face_return(data_structure)

print("Starting Main")
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
