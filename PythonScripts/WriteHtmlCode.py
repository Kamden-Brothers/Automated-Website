import os
from os import listdir
from os.path import isfile, join
mypath = r"C:\Users\kamde\nodejsPractice\HelloWorld\public\Images"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]






r"C:\\Users\\kamde\\nodejsPractice\\HelloWorld\\HTML\\Products\\"

inputFile = open(r"C:\Users\kamde\nodejsPractice\HelloWorld\public\Images\WebsiteVehicles.CSV", "r")

endOfFile = "end";
numberOfLines = 0;

while (inputFile.readline() != ''):
    numberOfLines += 1;


print(numberOfLines);

inputFile.seek(0);
numberOfItems = 10;
information = [""]*numberOfLines * numberOfItems

headerFirst = "<!DOCTYPE html> \n <html lang=\"en\" xmlns=\"http://www.w3.org/1999/xhtml\"> \n <head> \n <link rel=\"stylesheet\" href=\"../CSS/Header.css\"> \n <link rel=\"stylesheet\" href=\"../CSS/Products.css\"> \n <meta charset=\"utf-8\" /> \n <title>"
headerSecond = "</title> \n </head> \n <body> \n <div class=\"header\"> \n <h1> \n <a class=\"reference\" href=\"../HomePage.html\">Bros Auto </a> | <a class=\"reference\" href=\"../Inventory\"> Inventory Page </a> | <a class=\"reference\" href=\"../RepairShop.html\">Repair Shop </a> |<a class=\"reference\" href=\"../About.html\"> About</a> | <a class=\"reference\" href=\"../Parts.html\"> Parts Yard </a></h1> \n </div>"



i = 0;

while (i < numberOfLines):
    text = inputFile.readline();
    
    j = 0;
    typeOfInfo = 0;
    
    
    while(j < len(text)):
        placeHolder = "";
        while (text[j] != ","):
            placeHolder += text[j];
            j += 1;
            
            if (j == len(text)):
                break;
        
        placeHolder = placeHolder.replace("\"", "")
        information[typeOfInfo + i*numberOfItems] = placeHolder
        typeOfInfo += 1;
        
        j += 1;
    
    i += 1;

imagePlace = [""]*20;

placeHolderIMG = "..\\Resources\\CarLot.jpg"
br = "<br/>"


i = 0;
while (i < numberOfLines):
    print(information[1 + i*numberOfItems] + " " + information[2 + i*numberOfItems] + " " + information[3 + i*numberOfItems] + " ")
    
    numOfImages = 0;
    length = len(onlyfiles)
    
    imagePlace[0] = "..\\Resources\\CarLot.jpg"
    imgI=0
    while imgI < length:
        #print(onlyfiles[imgI][6:11])
        stockNum = information[0 + i*numberOfItems];
        if (onlyfiles[imgI][6:11] == stockNum):
            print(onlyfiles[imgI])
            imagePlace[numOfImages] = "..\\Images\\" + onlyfiles[imgI];
            numOfImages += 1;
            
            
        imgI = imgI+1


    

    baseDir = r"C:\\Users\\kamde\\nodejsPractice\\HelloWorld\\public\\Products\\";
    baseDir += information[6 + i*numberOfItems] + ".html";
    print (baseDir);
    
    file = open(baseDir , 'w')
    
    file.write(headerFirst)
    file.write(information[2 + i*numberOfItems] + information[3 + i*numberOfItems])
    file.write(headerSecond)
    
    content = "<table> <tr> <td > <img class=\"display\" src=\"" + imagePlace[0];
    content += "\" /> </td> <td class=\"information\"> <h2>";
    
    
    content += information[1 + i*numberOfItems] + " " + information[2 + i*numberOfItems] + " " + information[3 + i*numberOfItems] + "</h2>"
    
    content += "Transmission: " + information[4 + i*numberOfItems] + "<br />"
    content += "Engine: " + information[5 + i*numberOfItems] + "<br />"
    content += "Miles: " + information[7 + i*numberOfItems] + "<br />"
    content += "Color: " + information[8 + i*numberOfItems] + "<br />"
    content += "Price: $" + information[9 + i*numberOfItems] + "<br />"
    content += "Vin: " + information[6 + i*numberOfItems] + "<br />"
    
    content += "</td> </tr>"
    
    
    
    print(numOfImages%2)
    
    
    if (numOfImages%2 == 0 and numOfImages != 0):
        imagePlace[numOfImages] = placeHolderIMG;
        numOfImages += 1;
    
    j=1;
    while(j < numOfImages):
        
        if (j%2 == 1):
            content += "<tr>";
            
        content += " <td> <img class=\"display\" src=\"";
        content += imagePlace[j];
        content += "\" /> \n </td>";
        
        if (j%2 == 0):
            content += "\n </tr>";
        j += 1;
    
    if (j%2 == 1):
        content += "\n </tr>";
    
    content += "</table> \n <div class=\"footer\"> Business Hours: 8am-5pm Monday-Saturday. (Special meeting arrangements can be made if needed) \n <br />Contact us by call or text at (208)-466-9580 or by email at bros.auto@yahoo.com. \n <br />Or visit us at 3328 Caldwell Blvd, Nampa, Idaho. \n <br /> \n <p style=\"font-size:8px;text-align:right\">Website created by Kamden Brothers</p> \n </div> \n </body> \n </html>"
    
    file.write(content)
    
    i += 1;
    
    

#"C:\Users\kamde\nodejsPractice\WriteHtmlCode.py"





