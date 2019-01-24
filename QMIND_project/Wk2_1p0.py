# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 03:35:37 2019

@author: trist
"""

from PIL import Image
import binascii as bns
i = Image.open("testImage.jpg")

pixels = i.load() # this is not a list, nor is it list()'able
width, height = i.size

all_pixels = []
for x in range(width):
    for y in range(height):
        cpixel = pixels[x, y]
        all_pixels.append(cpixel)

#for x in range(width):
#    for y in range(height):
#        '#%02x%02x%02x' % all_pixels[x,y]

rgbData = (0,255,255)
for x in range(3):
    hexData = '0x%02x%02x%02x' % rgbData

print(hexData)