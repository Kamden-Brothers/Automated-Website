from PIL import Image

im = Image.open(r"C:\Users\kamde\Pictures\CarImages\IMG_1776.JPG");

newWidth = 700;
width = im.size[0];
height = im.size[1];

wpercent = (newWidth/float(width))
newHeight = int(float(height)*float(wpercent));

img = im.resize((newWidth,newHeight), Image.ANTIALIAS);
img.show();