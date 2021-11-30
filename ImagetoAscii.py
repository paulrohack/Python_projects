from  PIL import Image
import pygame as py
import cv2, sys

cap = cv2.VideoCapture(0)
cap.set(640, 0)
cap.set(480, 1)
py.font.init()

w = 5
b = py.Color('black')
white = py.Color('white')
font = py.font.SysFont("algerian", 10)
n = 0
char = ["#", "$", "0", "%", "+", "=", "|", "i", "-", ";", ".", " "]
WIN = py.display.set_mode((840, 680), py.RESIZABLE)
while True:
    _, image = cap.read()
    g = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = Image.fromarray(g)
    W, H = image.width + 200, image.height + 200
    image = image.resize((W , H))
    image = image.convert("L")
    WIN.fill(white)
    for x in range(0, W, w):
        for y in range(0, H, w):
            p = image.getpixel((x, y))
            if p >= 0 and p <= 20:
                    label = font.render(char[0], 0, b)
                    WIN.blit(label, (x, y))
            elif p > 20 and p <= 40:
                label = font.render(char[1], 0, b)
                WIN.blit(label, (x, y))
            elif  p > 40 and p <= 60:
                label = font.render(char[2], 0, b)
                WIN.blit(label, (x, y))
            elif  p > 60 and p <= 80:
                label = font.render(char[3], 0, b)
                WIN.blit(label, (x, y))
            elif  p > 80 and p <= 100:
                label = font.render(char[4], 0, b)
                WIN.blit(label, (x, y))
            elif  p > 100 and p <= 120:
                label = font.render(char[5], 0, b)
                WIN.blit(label, (x, y))
            elif  p > 120 and p <= 140:
                label = font.render(char[6], 0, b)
                WIN.blit(label, (x, y))
            elif  p > 140 and p <= 160:
                label = font.render(char[7], 0, b)
                WIN.blit(label, (x, y))
            elif  p > 160 and p <= 180:
                label = font.render(char[8], 0, b)
                WIN.blit(label, (x, y))
            elif  p > 180 and p <= 200:
                label = font.render(char[9], 0, b)
                WIN.blit(label, (x, y))
            elif  p > 200 and p <= 220:
                label = font.render(char[10], 0, b)
                WIN.blit(label, (x, y))
            elif  p > 220 and p <= 255:
                label = font.render(char[11], 0, b)
                WIN.blit(label, (x, y))
            #py.draw.rect(WIN, (p, p, p), (x, y, w, w))
    py.display.update()
    if cv2.waitKey(1) & 0xff == ord('q'):        
        break
    for events in py.event.get():
        if events.type == py.QUIT:
            py.quit()
            sys.exit()


    
