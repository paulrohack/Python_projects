import pygame as py
from math import pi, cos
import sys

H =  800
W =  1000

SIZE =  MASS = 100
CONSTANT = 2
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

    def physics(self, k, mass, b_color, s_color):
        md = W//2
        if self.posd:
            self.i += self.a
        if self.negd:
            self.i -= self.a


        if self.i > md - mass - 10:
            self.negd = True
            self.posd = False
        if self.i < self.s/4-md: 
            self.negd = False
            self.posd = True
        
        self.a =  ((k * md))/(mass)#ma = -kx 
        self.w = ((k/mass) ** 0.5)#k/m ** 1/2
        self.time = (2*pi * (1/self.w)) #2pi*1/w
        self.i_pos = (self.i * cos(self.w * self.time))
        py.draw.rect(self.root, b_color, (W//2 + self.x + self.i, self.y, self.s, self.s)) # body
        py.draw.line(self.root, s_color, (0, self.y + self.s//2), (W//2 + self.x + self.i, self.y + self.s//2), k) #spring
        py.draw.rect(self.root, py.Color('brown'), (0, self.y, 25, 100)) # fixed point

        return self.a, self.w, self.i_pos, self.time

bd = body(WIN, 10, (H - SIZE) - 10, SIZE)


while True:
    WIN.fill(0)
    py.time.Clock().tick(30)
    accelaration, angluar_accelaration, instantaneous_pos, time = bd.physics(CONSTANT, MASS, py.Color('green'), py.Color('red'))
    py.display.update()
    for events in py.event.get():
        if events.type == py.QUIT:
            print(f"SPEED FOR THE SPRING-MASS SYSTEM(IN ONE COMPLETE CYCLE): {round((W - 2 * SIZE)/ (time), 3)} m/s")
            py.quit()
            sys.exit()
        if events.type == py.MOUSEBUTTONUP:
            print(f"THEN INSTANTANEOUS POSITION OF THE SPRING-MASS SYSTEM: {instantaneous_pos}")
