import math, sys
import pygame as py

W, H = 800, 800
WIN = py.display.set_mode((W, H))

class Pendulum():
    def __init__(self, length, R, damping = False):
        self.originx, self.originy = W//2, 20
        self.bobx, self.boby  = 0, 0
        self.damping = damping
        self.length = length
        self.angle = math.pi/2
        self.gravity = 0.8
        self.R = R
        self.Angular_A = 0
        self.Angular_V = 0
        self.n = 0
        self.mass = self.R * 2
        
       
    def Draw(self):
        if py.mouse.get_pressed()[0]:
            if py.mouse.get_pos()[1] > 5:
                self.length = py.mouse.get_pos()[1]
            self.Angular_A = 0
            self.Angular_V = 0
            self.Pforce = 0
            self.angle = math.pi/2
            self.n = 0

        if self.n < self.bobx:
            self.n = self.bobx
        if self.damping:
            self.Pforce = (self.gravity * math.sin(self.angle) / self.length) + self.Angular_V/self.mass
        else:
            self.Pforce = (self.gravity * math.sin(self.angle) / self.length)

        self.Angular_A = (-1 * self.Pforce) / self.length
        self.Angular_V += self.Angular_A
        self.angle += self.Angular_V       
        self.bobx = self.length * math.sin(self.angle) + self.originx 
        self.boby = self.length * math.cos(self.angle) + self.originy
        py.draw.line(WIN, py.Color('black') , (self.originx, self.originy), (self.bobx, self.boby), 6)
        py.draw.circle(WIN, (176, 11, 105),(self.originx, self.originy), 7)
        py.draw.line(WIN, py.Color("cyan"), (self.bobx, self.boby), (self.bobx, H), 2)
        py.draw.line(WIN, py.Color("dark blue"), (self.n, H-10), (self.bobx, H-10), 10)
        py.draw.circle(WIN, py.Color("dark blue"), (self.bobx, self.boby), self.R)

        
pend = Pendulum(length=5, R=10, damping=True)

while True:
    WIN.fill((210, 224, 187))
    pend.Draw()

    py.display.update()
    for events in py.event.get():
        if events.type == py.QUIT:
            py.quit()
            sys.exit()