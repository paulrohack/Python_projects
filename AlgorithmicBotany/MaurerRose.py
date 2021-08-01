import math
import pygame as py

print("In geometry, the concept of a Maurer rose was introduced by Peter M. Maurer in his article titled A 'Rose is a Rose'. A Maurer rose consists of some lines that connect some points on a rose curve.\n")
n = int(input("[N]umber of Petals (n is EVEN: n*2; n is ODD: n) = "))
d = int(input("Number of [L]egs in the Petals = "))

def line(surface, color, s_pos, e_pos, thickness):
    py.draw.line(surface, color, s_pos, e_pos, thickness)


W, H = 800, 800
WIN = py.display.set_mode((W, H))
sx, sy = W//2, H//2

while True:
    if py.mouse.get_pressed()[2]:
        area = py.Rect(0, 0, W, H)
        screenShot = WIN.subsurface(area)
        print('Screenshot Saved')
        py.image.save(WIN,f"AlgorithmicBotany\\Images\\MaurerRose[{n,d}].png")
    for i in range(361):
        k = i * d * math.pi / 180
        r = 300 * math.sin(n * k)
        x = r * math.cos(k) + W//2
        y = r * math.sin(k) + H//2
        line(WIN, py.Color('blue'), (sx,sy), (x,y), 2)
        sx = x
        sy = y
    for i in range(361):
        k = i * math.pi / 180
        r = 300 * math.sin(n * k)
        x = r * math.cos(k) + W//2
        y = r * math.sin(k) + H//2
        line(WIN, py.Color('red'), (sx,sy), (x,y), 4)
        sx = x
        sy = y

    py.display.update()
    for events in py.event.get():
        if events.type == py.QUIT:
            py.quit()
