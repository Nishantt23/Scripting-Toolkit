import pytesseract
import sys

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
print(pytesseract.image_to_string(r'C:\Users\Nishant\Desktop\s1.PNG'))