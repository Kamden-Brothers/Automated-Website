#Finds an images that corresponds within the csv file uploaded from Frazer and appends one to the end of each data entry
#If no image corresponds it inputs a generic photo of the car lot.

from os import listdir
from os.path import isfile, join
mypath = r"C:\Users\kamde\nodejsPractice\HelloWorld\public\Images" 
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]   #finds all files within a folder


length = len(onlyfiles)

imageDoc = open(r"C:\Users\kamde\nodejsPractice\HelloWorld\public\JavaScript\WebsiteVehicles.CSV", "w")

imgFiles = [];

i=0
while i < length:
 if (onlyfiles[i][0:5] == "56060"):
  imgFiles.append(onlyfiles[i])
 i = i+1


numOfImg = len(imgFiles)

inputFile = open(r"C:\Users\kamde\nodejsPractice\HelloWorld\public\Images\WebsiteVehicles.CSV", "r")

numberOfLines = 0;
text = inputFile.readline()



fullText = "placeholder\n"

while(True):
    text = text[0:len(text)-1]
    numberOfLines += 1
    
    allInfo = "";
    stockNumber = "";
    i = 0;
    while(text[i] != ","):
        stockNumber += text[i];
        
        i += 1
    
    stockNumber = stockNumber.replace("\"", "")
    
    fullText += text + ",\""
    
    found = False
    i = 0
    while(i < numOfImg):
        #print(stockNumber)
        if (imgFiles[i][6:11] == stockNumber):
            fullText += "../Images/" + imgFiles[i]
            found = True
            break
        i += 1
    
    if(found == False):
        fullText += "../Resources/CarLot.jpg"
    
    fullText += "\"," + text.replace(",", "") + "\n"
    fullText = fullText.replace("\"", "")
    text = inputFile.readline()
    
    
    if (text == ''):
        break;

imageDoc.write(fullText)
