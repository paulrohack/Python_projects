import math
import pygame as py

W, H = 600, 600
WIN = py.display.set_mode((W, H))

class Pendulum():
    def __init__(self, length, R):
        self.originx, self.originy = W//2, 20
        self.bobx, self.boby  = 0, 0
        self.length = length
        self.angle = math.pi/4
        self.gravity = 0.8
        self.R = R
        self.Angular_A = 0
        self.Angular_V = 0

       
    def Draw(self):
        self.Pforce = self.gravity * math.sin(self.angle) / self.length
        self.Angular_A = (-1 * self.Pforce) / self.length
        self.Angular_V += self.Angular_A
        self.angle += self.Angular_V       
        self.bobx = self.length * math.sin(self.angle) + self.originx
        self.boby = self.length * math.cos(self.angle) + self.originy
        py.draw.line(WIN, py.Color('black') , (self.originx, self.originy), (self.bobx, self.boby), 6)
        py.draw.circle(WIN, (176, 11, 105),(self.originx, self.originy), 7)
        py.draw.circle(WIN, py.Color("dark blue"), (self.bobx, self.boby), self.R)
        py.draw.circle(WIN, py.Color("cyan"), (self.bobx, self.boby), self.R - 15) #Origin
        



length = int(input("lenght of The String: ")) * 10
pend = Pendulum(length, 20)

while True:
    WIN.fill((210, 224, 187))
    pend.Draw()

    

    py.display.update()
    for events in py.event.get():
        if events.type == py.QUIT:
            py.quit()