import pygame as py
import random, math
py.init()

def pixel(surface, color, pos, thickness):
        py.draw.circle(surface, color, pos, thickness)

print("In mathematics, a rose or rhodonea curve is a sinusoid specified by either the cosine or sine functions with no phase angle that is plotted in polar coordinates.\n")
n = int(input("N = "))
d = int(input("D = "))
k = n/d
a = 0

W, H = 800, 800
WIN = py.display.set_mode((W, H))
while True:
    if(a <= 360):
        a += 0.01
        r = 200 * math.cos(k * a)
        x = r * math.cos(a) + W//2
        y = r * math.sin(a) + H//2
        pixel(WIN, py.Color('blue'), (x, y), 1.5)
    else:
        pass
    py.display.update()
    for events in py.event.get():
        if events.type == py.QUIT:
            py.quit()



