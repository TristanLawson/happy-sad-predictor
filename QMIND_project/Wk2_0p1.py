# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 16:16:06 2019

@author: trist
"""
from __future__ import print_function
from PIL import Image, ImageFilter

#functions_____________________________________________________________________

#rotates the top half of an image 180 degrees and pastes it on the original
def flipTop(image):
    region = (0,0,image.size[0],image.size[1]/2)
    crop = image.crop(region)
    crop = crop.transpose(Image.ROTATE_180)
    image.paste(crop)
    return image

#crops bottom and right-side of images to make them equal size **doesn't work**
def findEqualSize(image1,image2):
    width = min(image1.size[0],image2.size[0])
    height = min(image1.size[1],image2.size[1])
    region = (0,0,width,height)
    return region

#"sunny" version of an image
def showLight(image):
    out = image.point(lambda i: i * 5)
    return out

#"night" version of an image
def showDark(image):
    out = image.point(lambda i: i / 5)
    return out

#import images_________________________________________________________________
im1 = Image.open("stop01.ppm")
im2 = Image.open("stop02.ppm")


#main function_________________________________________________________________

r, g, b = im1.split()
im = Image.merge("RGB", (b, g, r))

im.show()















