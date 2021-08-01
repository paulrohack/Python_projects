import pytesseract
import cv2, numpy
from PIL import Image, ImageGrab
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\paulr\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

# cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
screenshot = ImageGrab.grab()
converted = numpy.array(screenshot)
converted = cv2.cvtColor(converted, cv2.COLOR_BGR2RGB)
t = cv2.selectROI(converted, False)
x, y, w, h = t
if x + y + w + h != 0:
    converted = screenshot.crop((x, y, x + w, y + h))
    img = numpy.array(converted)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.destroyWindow('ROI selector')
# path = 'OCR\Image(2).jpg'
# img = cv2.imread(path) 

t = []
l = True
while True:
    cv2.imshow('OCR', img)
    word = pytesseract.image_to_data(img)
    word = word.splitlines()
    if l:
        for e, i in enumerate(word):
            if e != 0:
                i = i.split()
                x, y, w, h = (int(i[6]), int(i[7]), int(i[8]), int(i[9]))
                if len(i) == 12:
                    text = i[11]
                    t.append(text.upper())
                    cv2.rectangle(img,(x, y), (x+w, y+h) , (255, 0, 0))
                    # cv2.putText(img, text, (x, y), font, 0.5, (0, 0, 255), 2) 
            if e == len(word)-1:
                t = str(t).replace(', ', ' ').replace("'", '')
                if t == '[]':
                    print("NOTHING RECOGNIZED")
                    
                else:
                    print("RECOGNIZED : " + t)
                l = False          
    else:
        break 
    if cv2.waitKey(1) & 0xff == ord('q'):     
        break