from PIL import Image
from os import listdir
import os
from os.path import isfile, join
mypath = r"C:\Users\kamde\Pictures\CarImages"

try:
    os.mkdir(mypath + r"\lowerRes")
except OSError as error:
    print("directory exists")
    
allFiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

imgFiles = []

for oneFile in allFiles:
    length = len(oneFile)
    print(length)
    print(oneFile[(length-3):(length)])
    if(oneFile[(length-3):(length)] == "JPG"):
       imgFiles.append(oneFile)


for imgFile in imgFiles:

    im = Image.open(mypath + "/" + imgFile);

    newWidth = 700;
    width = im.size[0];
    height = im.size[1];

    wpercent = (newWidth/float(width))
    newHeight = int(float(height)*float(wpercent));

    im = im.resize((newWidth,newHeight), Image.ANTIALIAS);
    #im.show();
    im.save(mypath + imgFile);