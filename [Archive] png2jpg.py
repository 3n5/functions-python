"""Convert png to jpg"""
import os
import sys
from PIL import Image
import glob
import time

#Folder with png
target_dir = r"C:/Users/USER/Desktop/png_folder" 


#make save folder
dirname, basename = os.path.split(target_dir )
save_dir=os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "/Desktop/"+basename+"_jpg/"
if not os.path.exists(save_dir): 
    os.makedirs(save_dir)

#png 
def png2jpg(path_png,path_jpg):
    image = Image.open(path_png).convert('P')
    image.save(path_png)
    rgb_im = Image.open(path_png).convert('RGB')
    rgb_im.save(path_jpg)

files = glob.glob(target_dir + '/*')
data=[]
print(len(files)*0.1/60,' sec')
for file in files:
    dirname, basename = os.path.split(file) 
    root, ext = os.path.splitext(basename)
    path_jpg=save_dir+root+'.jpg'
    png2jpg(file,path_jpg)
    time.sleep(0.1)
