from  math import sin, cos, sqrt
import pygame as py


W, H = 600, 600
WIN = py.display.set_mode((W, H))
py.display.set_caption('PhyllotAxis Visualization')
n = 0
c = 3

points =[]
start = 0

def map(value, min1, max1, min2, max2):
    return min2 + (max2 - min2)* ((value-min1)/(max1-min1))
def pixel(surface, color, pos, thickness):
        py.draw.circle(surface, color, pos, thickness)
def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
 
    # h, s, v = hue, saturation, value
    cmax = max(r, g, b)    # maximum of r, g, b
    cmin = min(r, g, b)    # minimum of r, g, b
    diff = cmax-cmin       # diff of cmax and cmin.
 
    # if cmax and cmax are equal then h = 0
    if cmax == cmin:
        h = 0
     
    # if cmax equal r then compute h
    elif cmax == r:
        h = (60 * ((g - b) / diff) + 360) % 360
 
    # if cmax equal g then compute h
    elif cmax == g:
        h = (60 * ((b - r) / diff) + 120) % 360
 
    # if cmax equal b then compute h
    elif cmax == b:
        h = (60 * ((r - g) / diff) + 240) % 360
 
    # if cmax equal zero
    if cmax == 0:
        s = 0
    else:
        s = (diff / cmax) * 100
 
    # compute v
    v = cmax * 100
    return h, s, v
angle = 0

while True:
    
    #

    
    if py.mouse.get_pressed()[0]:
        mouse = py.mouse.get_pos()
        angle = int(map(mouse[0], 0, W, 0, 200))
    if py.mouse.get_pressed()[2]:
        area = py.Rect(0, 0, W, H)
        screenShot = WIN.subsurface(area)
        print('Screenshot Saved')
        py.image.save(WIN,f"AlgorithmicBotany\\ImagesPhyllotAxis[{angle}].png")
    WIN.fill(py.Color('black'))
    offX, offY = W//2, H//2
    py.time.Clock().tick(20)

    for i in range(0, n):
        a = i * angle
        r = c * sqrt(i)
        x = r * cos(a)
        y = r * sin(a)
        color = 155 - sin(start + i) * i
        if color <= 0:
            color = 1
        elif color >= 255:
            color = 254
        #print(color)
        pixel(WIN, rgb_to_hsv(color, 105, 105), (x + offX, y + offY), 3.75)


        i += 1
    n += 10
    start += 10

    py.display.update()
    for events in py.event.get():
        if events.type == py.QUIT:
            py.quit()