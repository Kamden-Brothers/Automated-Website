from PIL import Image
from os import listdir
import os
from os.path import isfile, join
mypath = r"C:\Users\kamde\Pictures\CarImages"                               #Folder with images that need to be resized.

allFiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]          #this finds all files within a given directory

imgFiles = []

for oneFile in allFiles:
    length = len(oneFile)
    print(length)
    print(oneFile[(length-3):(length)])
    if(oneFile[(length-3):(length)] == "JPG"):          #checks for all JPG within the folder
       imgFiles.append(oneFile)                         


for imgFile in imgFiles:        #resizes each image

    im = Image.open(mypath + "/" + imgFile);

    newWidth = 700;                                     #new width dimension
    width = im.size[0];
    height = im.size[1];

    wpercent = (newWidth/float(width))                  #finds the ratio between new width and the old width
    newHeight = int(float(height)*float(wpercent));     #multiplies height by that ration

    im = im.resize((newWidth,newHeight), Image.ANTIALIAS);
    im.save(mypath + imgFile);                  #could create a new path to save if you want to save the original images
