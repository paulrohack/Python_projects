import pygame as py

SIZE = 100
W =  1000
H =  SIZE * 4
WIN = py.display.set_mode((W, H))
class body:
    def __init__(self, root, x, y, s):
        self.x = x
        self.y = y
        self.s = s
        self.root = root
        self.a = 0
        self.i = 0
        self.posd, self.negd = True, False

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
        self.a =  (k * md)/(mass)

        py.draw.rect(self.root, b_color, (self.x + self.i, self.y, self.s, self.s)) # body
        py.draw.line(self.root, s_color, (0, self.y + self.s//2), (self.x + self.i, self.y + self.s//2), k) #spring

bd = body(WIN, 10, (H - SIZE) - 10, SIZE)
while True:
    WIN.fill(0)
    py.time.Clock().tick(30)
    bd.physics(1, W - SIZE, SIZE, py.Color('green'), py.Color('red'))
    py.display.update()
    for events in py.event.get():
        if events.type == py.QUIT:
            py.quit()