#!/usr/bin/env python
# coding: utf-8

# # Assignment 1: Building a Better Contact Sheet
# In the lectures for this week you were shown how to make a contact sheet for digital photographers, and how you can take one image and create nine different variants based on the brightness of that image. In this assignment you are going to change the colors of the image, creating variations based on a single photo. There are many complex ways to change a photograph using variations, such as changing a black and white image to either "cool" variants, which have light purple and blues in them, or "warm" variants, which have touches of yellow and may look sepia toned. In this assignment, you'll be just changing the image one color channel at a time
# 
# Your assignment is to learn how to take the stub code provided in the lecture (cleaned up below), and generate the following output image:
# 
# ![](./readonly/assignment1.png "")
# 
# From the image you can see there are two parameters which are being varied for each sub-image. First, the rows are changed by color channel, where the top is the red channel, the middle is the green channel, and the bottom is the blue channel. Wait, why don't the colors look more red, green, and blue, in that order? Because the change you to be making is the ratio, or intensity, or that channel, in relationship to the other channels. We're going to use three different intensities, 0.1 (reduce the channel a lot), 0.5 (reduce the channel in half), and 0.9 (reduce the channel only a little bit).
# 
# For instance, a pixel represented as (200, 100, 50) is a sort of burnt orange color. So the top row of changes would create three alternative pixels, varying the first channel (red). one at (20, 100, 50), one at (100, 100, 50), and one at (180, 100, 50). The next row would vary the second channel (blue), and would create pixels of color values (200, 10, 50), (200, 50, 50) and (200, 90, 50).
# 
# Note: A font is included for your usage if you would like! It's located in the file `readonly/fanwood-webfont.ttf`
# 
# Need some hints? Use them sparingly, see how much you can get done on your own first! The sample code given in the class has been cleaned up below, you might want to start from that.

# In[36]:


import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFont, ImageDraw




# Instantiate arrays
green_array = []
blue_array = []
red_array = []

def build_arrays(red, green, blue):
    # read image and convert to RGB
    image=Image.open("readonly/msi_recruitment.gif")
    image=image.convert('RGB')
    
    # build arrays with standard images
    for i in range (0,3):
        green.append(image.copy())
       
        blue.append(image.copy())
    
        red.append(image.copy())
       
    

def write_text(red, green, blue):
    
    #Set up font text
    font = ImageFont.truetype("readonly/fanwood-webfont.ttf", 50)
    #Get a defualt image
    first_image=red[0]
    for i in range(0,3):
        if i == 0:
            #write text
            #1 Set Draw
            #2 Draw Rectangle
            # Draw Text
            
            draw = ImageDraw.Draw(red[i])
            draw.rectangle((0, first_image.height - 50, first_image.width, first_image.height ), fill='black')
            draw.text((10, first_image.height-50), "channel 0 intensity 0.1", font=font)
            
            draw = ImageDraw.Draw(green[i])
            draw.rectangle((0, first_image.height - 50, first_image.width, first_image.height ), fill='black')
            draw.text((10, first_image.height-50), "channel 1 intensity 0.1", font=font)
            
            draw = ImageDraw.Draw(blue[i])
            draw.rectangle((0, first_image.height - 50, first_image.width, first_image.height ), fill='black')
            draw.text((10, first_image.height-50), "channel 2 intensity 0.1", font=font)



        elif i == 1:
             #write text
            #1 Set Draw
            #2 Draw Rectangle
            # Draw Text
           
           
            draw = ImageDraw.Draw(red[i])
            draw.rectangle((0, first_image.height - 50, first_image.width, first_image.height ), fill='black')
            draw.text((10, first_image.height-50), "channel 0 intensity 0.5", font=font)
            
            draw = ImageDraw.Draw(green[i])
            draw.rectangle((0, first_image.height - 50, first_image.width, first_image.height ), fill='black')
            draw.text((10, first_image.height-50), "channel 1 intensity 0.5", font=font)
            
            draw = ImageDraw.Draw(blue[i])
            draw.rectangle((0, first_image.height - 50, first_image.width, first_image.height ), fill='black')
            draw.text((10, first_image.height-50), "channel 2 intensity 0.5", font=font)


        elif i == 2:
             #write text
            #1 Set Draw
            #2 Draw Rectangle
            # Draw Text
            
            draw = ImageDraw.Draw(red[i])
            draw.rectangle((0, first_image.height - 50, first_image.width, first_image.height ), fill='black')
            draw.text((10, first_image.height-50), "channel 0 intensity 0.9", font=font)
            
            draw = ImageDraw.Draw(green[i])
            draw.rectangle((0, first_image.height - 50, first_image.width, first_image.height ), fill='black')
            draw.text((10, first_image.height-50), "channel 1 intensity 0.9", font=font)
            
            draw = ImageDraw.Draw(blue[i])
            draw.rectangle((0, first_image.height - 50, first_image.width, first_image.height ), fill='black')
            draw.text((10, first_image.height-50), "channel 2 intensity 0.9", font=font)



def modify_colors(red,green,blue):
    #Set Default R, G, B Source Values
    R, G, B = 0, 1, 2
    for i in range(0 , 3):
        if i == 0:
            #Modify intensity 0.1 RGB
            #Set Source
            sourceRed = red[i].split()
            sourceGreen = green[i].split()
            sourceBlue = blue[i].split()

            # process the red band
            out = sourceRed[R].point(lambda x: x * 0.1)
            # paste the processed band back
            sourceRed[R].paste(out, None)
            # build a new multiband image
            red[i] = Image.merge(red[i].mode, sourceRed)

            # process the Green band
            out = sourceGreen[G].point(lambda x: x * 0.1)
            # paste the processed band back
            sourceGreen[G].paste(out, None)
            # build a new multiband image
            green[i] = Image.merge(green[i].mode, sourceGreen)

            # process the blue band
            out = sourceBlue[B].point(lambda x: x * 0.1)
            # paste the processed band back
            sourceBlue[B].paste(out, None)
            # build a new multiband image
            blue[i] = Image.merge(blue[i].mode, sourceBlue)



        elif i == 1:
            #Modify intensity 0.5 RGB
            #Set Source
            sourceRed = red[i].split()
            sourceGreen = green[i].split()
            sourceBlue = blue[i].split()

            # process the red band
            out = sourceRed[R].point(lambda x: x * 0.5)
            # paste the processed band back
            sourceRed[R].paste(out, None)
            # build a new multiband image
            red[i] = Image.merge(red[i].mode, sourceRed)

            # process the Green band
            out = sourceGreen[G].point(lambda x: x * 0.5)
            # paste the processed band back
            sourceGreen[G].paste(out, None)
            # build a new multiband image
            green[i] = Image.merge(green[i].mode, sourceGreen)

            # process the blue band
            out = sourceBlue[B].point(lambda x: x * 0.5)
            # paste the processed band back
            sourceBlue[B].paste(out, None)
            # build a new multiband image
            blue[i] = Image.merge(blue[i].mode, sourceBlue)


        elif i == 2:
            #Modify intensity 0.9 RGB
            #Set Source
            sourceRed = red[i].split()
            sourceGreen = green[i].split()
            sourceBlue = blue[i].split()

            # process the red band
            out = sourceRed[R].point(lambda x: x * 0.9)
            # paste the processed band back
            sourceRed[R].paste(out, None)
            # build a new multiband image
            red[i] = Image.merge(red[i].mode, sourceRed)

            # process the Green band
            out = sourceGreen[G].point(lambda x: x * 0.9)
            # paste the processed band back
            sourceGreen[G].paste(out, None)
            # build a new multiband image
            green[i] = Image.merge(green[i].mode, sourceGreen)

            # process the blue band
            out = sourceBlue[B].point(lambda x: x * 0.9)
            # paste the processed band back
            sourceBlue[B].paste(out, None)
            # build a new multiband image
            blue[i] = Image.merge(blue[i].mode, sourceBlue)



def copy_to_contactSheet(red,green,blue):
    stockImage=Image.open("readonly/msi_recruitment.gif")
    stockImage=stockImage.convert('RGB')
    contact_sheet=PIL.Image.new(stockImage.mode, (stockImage.width*3,stockImage.height*3))
    x=0
    y=0

    for i in range(0,3):
        if i == 0:
        #Paste 0.1 intensity bands
            #Paste Red band
            contact_sheet.paste(red[i], (x, y) )
            y = y + stockImage.height

            #Paste Green band
            contact_sheet.paste(green[i], (x, y) )
            y = y + stockImage.height

            #Paste Blue band
            contact_sheet.paste(blue[i], (x, y) )
            y = y + stockImage.height

        if i == 1:
        #Paste 0.1 intensity bands
            #Update x and y Positions
            x = x + stockImage.width
            y = 0
            
            #Paste Red band
            contact_sheet.paste(red[i], (x, y) )
            y = y + stockImage.height

            #Paste Green band
            contact_sheet.paste(green[i], (x, y) )
            y = y + stockImage.height

            #Paste Blue band
            contact_sheet.paste(blue[i], (x, y) )
            y = y + stockImage.height

        if i == 2:
        #Paste 0.1 intensity bands
            #Update x and y
            x = x + stockImage.width
            y = 0
            
            #Paste Red band
            contact_sheet.paste(red[i], (x, y) )
            y = y + stockImage.height

            #Paste Green band
            contact_sheet.paste(green[i], (x, y) )
            y = y + stockImage.height

            #Paste Blue band
            contact_sheet.paste(blue[i], (x, y) )
            y = y + stockImage.height

    return contact_sheet

build_arrays(red_array,green_array,blue_array)

write_text(red_array,green_array,blue_array)

modify_colors(red_array,green_array,blue_array)

contact_sheet = copy_to_contactSheet(red_array,green_array,blue_array)

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2)))
display(contact_sheet)



# ## HINT 1
# 
# Check out the `PIL.ImageDraw module` for helpful functions

# ## HINT 2
# 
# Did you find the `text()` function of `PIL.ImageDraw`?

# ## HINT 3
# 
# Have you seen the `PIL.ImageFont` module? Try loading the font with a size of 75 or so.

# ## HINT 4
# These hints aren't really enough, we should probably generate some more.
