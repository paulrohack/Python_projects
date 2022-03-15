import pygame as py
from random import choice 
import sys 

W, H = 600, 600
WIN = py.display.set_mode((W, H))

def lerp(a1, a2, t):
    lx = a1[0] + (a2[0] - a1[0]) * t
    ly = a1[1] + (a2[1] - a1[1]) * t
    return (lx, ly)

def cubic(a2, b2, c2, d2, t, draw = False):
    def quadratic(a1, b1, c1, t):
        l1 = lerp(a1, b1, t)
        l2 = lerp(b1, c1, t)
        if draw:
            py.draw.line(WIN, (255 * t, 255 * t, 255), l1, l2)
        return lerp(l1, l2, t)
    l1 = quadratic(a2, b2, c2, t)
    l2 = quadratic(b2, c2, d2, t)
    if draw:
        py.draw.line(WIN, (255 * t, 255, 255 * t), l1, l2)
    return lerp(l1, l2, t)

a = 100, H/2
m = 200, 500
b = 400, 100
c = 500, H/2
while True:
    WIN.fill(0)
    if py.mouse.get_pressed()[0]:
        m = py.mouse.get_pos()
    if py.mouse.get_pressed()[2]:
        b = py.mouse.get_pos()

    t = 0
    while t <= 1: 
        l = cubic(a, m, b, c, t, True)
        py.draw.circle(WIN, py.Color('white'), l, 3)
        t += 0.05

    py.draw.circle(WIN, py.Color('blue'), a, 8)
    py.draw.circle(WIN, py.Color('red'), b, 8)
    py.draw.circle(WIN, py.Color('yellow'), c, 8)
    py.draw.circle(WIN, py.Color('pink'), m, 8)

    py.time.Clock().tick(60)
    py.display.update()
    for events in py.event.get():
        if events.type == py.QUIT:       
            py.quit()
            sys.exit()