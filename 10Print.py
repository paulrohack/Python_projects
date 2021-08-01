import pygame as py
from random import choice  

W, H = 600, 600
WIN = py.display.set_mode((W, H))

WIN.fill(py.Color('#3333ff'))

color = '#8080ff'
w = 20
x, y = 0, 0
t = 8
i = 0

while True:
    py.time.Clock().tick(60)
    s = choice([0, 1])
    if s == 0:
      py.draw.line(WIN, color, (x, y), (x + w, y + w), width=t)
    else:
        py.draw.line(WIN, color, (x, y + w), (x + w, y), width=t)
    if (x > W) :
        y += w
        x = 0
        i += 1
    elif y < H and i != 30:
        x += w

    py.display.update()
    for events in py.event.get():
        if events.type == py.QUIT:
            py.quit()