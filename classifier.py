try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

inImage = '_assets/numtest.png'
img_cv = cv2.imread(inImage,0)

img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img_rgb))