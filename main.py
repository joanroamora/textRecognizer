##Imports the neccesary libraries
from PIL import Image
from pytesseract import *

##Research for the Tesseract Software installation directory
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

##Remember that the image file must be stored in the main.py directory. 
##Note the spelling of the image file name and replace the values in the following line of code. 
img = Image.open("image.jpg")

##The information becomes a string variable.
devResult = pytesseract.image_to_string(img)

print(devResult)
