##Imports the neccesary libraries
from PIL import Image
from pytesseract import *

##Research for the Tesseract Software installation directory
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


img = Image.open("image.jpg")

devResult = pytesseract.image_to_string(img)

print(devResult)