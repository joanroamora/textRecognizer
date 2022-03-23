DESCRIPTION
This solution is a software designed to take your images with text and transform them into a plain text, 
searchable and manipulable from digital media. To do so, you will have to follow the installation steps that you can read below. 
Please make sure that the image you intend to convert into text has clear characters, it is essential to fulfill what is promised. 

PROJECT STATE
The project is ready and available for operation. 
It may be subject to modifications that will be uploaded to the main repository -main-.

REQUIREMENTS
Our solution is available for Windows operating systems, both 32-bit and 64-bit.
You need to have the latest version of Python and the Tesseract installer for Windows. 
Both and in the same order you can find them in the following links:

-https://www.python.org/downloads/
-https://github.com/UB-Mannheim/tesseract/wiki

INSTALLATION AND OPERATION GUIDE
Instalation: 
-Verify that you have a recent version of Python installed on your computer.
-Verify that the pip command is available in your environment. If not, install Python and give it the ability to modify the PATH.
-Install tesseract-ocr in its 32-bit or 64-bit version according to the architecture of your computer.
-If you want to recognize text in a language other than English, install the additional language library, 
which you can select in the tesseract installation process. 
-You need to download the piTesseract and pillow packages, the former to be able to use the tesseract software with 
Python and the latter to be able to directly use image files within the programming language. The installation commands are as follows:

pip install pytesseract

pip install Pillow

Remember to run the pip install pytesseract command only until the installation of the Tesseract software is complete. 
Otherwise you may get errors in the installation process.

Now enter the main.py file, and through the text editor of your choice modify the code according to your needs. 
You will find a few lines of comment code with specific indications in each section of the code.
