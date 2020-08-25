"""png to jpg"""
import os
import cv2
import sys
import numpy as np
from PIL import Image

path_png = "C:/Users/USER/Downloads/download.png"
path_jpg = "C:/Users/USER/Downloads/download.jpg"

image = Image.open(path_png).convert('P')
image.save(path_png)
rgb_im = Image.open(path_png).convert('RGB')
rgb_im.save(path_jpg)

print("fin")

