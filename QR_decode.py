from pyzbar.pyzbar import decode
from PIL import Image
import cv2
import webbrowser
import pyperclip as pc

webcam = True
path = "H:\\Python\\Qr_Images\\1.png"
if webcam: 
    cap = cv2.VideoCapture(1)
    thickness = 2
else: 
    thickness = 1
    img = cv2.imread(path)

text = ''
ptext = ''
while True:
    if webcam: _, img = cap.read()
    
    p = decode(Image.fromarray(img))
    if p != []:
        rect = p[0].rect
        text = (p[0].data).decode('utf-8')
        if ptext != text:
            print(text + " >>> Text is copied to your clipboard")
            if "//" in text :
                webbrowser.open_new(text)
            else:
                pc.copy(text)
        cv2.rectangle(img, (rect.left, rect.top), (rect.left+rect.width, rect.top+rect.height), (255, 0, 0), 2)
        cv2.putText(img, text, (rect.left, rect.top), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), thickness)
        
    cv2.imshow("window", img)
    ptext = text
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
