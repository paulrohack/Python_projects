import pygame as py
from math import pi, cos
import sys

H =  800
W =  1000

SIZE =  MASS = 100
CONSTANT = 1
MAX_DISTANCE = W - SIZE

WIN = py.display.set_mode((W, H))
class body:
    def __init__(self, root, x, y, s):
        self.x = x
        self.y = y
        self.s = s
        self.root = root
        self.a = 0
        self.w = 0
        self.i = 0
        self.i_pos = 0
        self.posd, self.negd = True, False
        self.time = 0

    def physics(self, k, md, mass, b_color, s_color):
        if self.posd:
            self.i += self.a
        if self.negd:
            self.i -= self.a

        if self.i > md :
            self.negd = True
            self.posd = False
        if self.i < 5: 
            self.negd = False
            self.posd = True
        
        self.a =  (k * md)/(mass) #ma = -kx
        self.w = ((mass/k) ** 0.5)#m/k ** 1/2
        self.time = (2*pi * self.w) #2pi*w
        self.i_pos = (self.i * cos(self.w * self.time))
        py.draw.rect(self.root, b_color, (self.x + self.i, self.y, self.s, self.s)) # body
        py.draw.line(self.root, s_color, (0, self.y + self.s//2), (self.x + self.i, self.y + self.s//2), k) #spring
        py.draw.rect(self.root, py.Color('brown'), (0, self.y, self.s/4, self.s)) # fixed point

        return self.a, self.w, self.i_pos, self.time

bd = body(WIN, 10, (H - SIZE) - 10, SIZE)


while True:
    WIN.fill(0)
    py.time.Clock().tick(30)
    accelaration, angluar_accelaration, instantaneous_pos, time = bd.physics(CONSTANT, MAX_DISTANCE, MASS, py.Color('green'), py.Color('red'))
    py.display.update()
    for events in py.event.get():
        if events.type == py.QUIT:
            print(f"TIME TAKEN FOR THE SPRING-MASS SYSTEM(IN ONE DIRECTION): {round(time/2, 3)}")
            py.quit()
            sys.exit()
        if events.type == py.MOUSEBUTTONUP:
            print(f"THEN INSTANTANEOUS POSITION OF THE SPRING-MASS SYSTEM: {instantaneous_pos}")
