import pygame as py
from matplotlib import pyplot as plt
import sys

import time
W, H = 600, 600
WIN = py.display.set_mode((500, H))

def map(value, min1, max1, min2, max2):
    return min2 + (max2 - min2)* ((value-min1)/(max1-min1))

max_iteration = 100
WIN.fill((0, 0, 0))
m = []

for xp in range(0, W, 1):
    for yp in range(0, H, 1):
        a = map(xp, 0, W, -2, 2)
        b = map(yp, 0, H, -2, 2)
        ca = a 
        cb = b 
        n = 0
        while (n < max_iteration):
            aa = a*a - b*b
            bb = 2*a*b
            a = aa + ca
            b = bb + cb
            if (a*a + b*b > 16):
                break
            n += 1
        bright = map(n, 0, max_iteration, 0, 1);
        bright = map(bright, 0, 1, 0, 255);
        if (n == max_iteration):
            bright = 0;
        py.draw.rect(WIN, (bright, bright, 51), (xp , yp  , 1, 1))
while True:
    py.display.update()
    for events in py.event.get():
        if events.type == py.QUIT:
            py.quit()
            sys.exit()