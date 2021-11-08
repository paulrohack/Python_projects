import pygame
W, H = 600, 600
WIN = pygame.display.set_mode((W, H))
WIN.fill(pygame.Color('white'))
class Gradient_lines:
    def __init__(self, s_pos : tuple, f_pos : tuple, h : int, color_inc : tuple, root : pygame.Surface,  FPS = 60):
        self.s_pos = s_pos
        self.FPS = FPS
        self.h = h
        self.color_inc = color_inc
        self.r, self.g, self.b = self.color_inc[0], self.color_inc[1], self.color_inc[2]
        self.root = root
        self.f_pos = f_pos
        self.red, self.green, self.blue = 0, 0, 0
        self.i = 0
    def draw(self):
        pygame.time.Clock().tick(self.FPS)
        if self.i < self.h:
            if self.red < 254: self.red += self.r
            if self.blue < 254: self.blue += self.b
            if self.green < 254: self.green += self.g
            self.i += 1
        pygame.draw.line(self.root, (self.red, self.green, self.blue), (self.s_pos[0], self.s_pos[1] + self.i), (self.f_pos[0], self.f_pos[1] + self.i))

class Gradient_circles:
    def __init__(self, pos : tuple, rad : int, color_inc : tuple, root : pygame.Surface,  FPS = 60):
        self.pos = pos
        self.FPS = FPS
        self.rad = rad
        self.color_inc = color_inc
        self.r, self.g, self.b = self.color_inc[0], self.color_inc[1], self.color_inc[2]
        self.root = root
        self.red, self.green, self.blue = 10, 10, 10
        if self.r >= 1: self.red = self.r * 50
        if self.g >= 1: self.green  = self.g * 50
        if self.b >= 1: self.blue  = self.b * 50
        self.i = 0
    def draw(self):
        pygame.time.Clock().tick(self.FPS)
        if self.i < self.rad:
            if self.red < 254: self.red += self.r
            if self.blue < 254: self.blue += self.b
            if self.green < 254: self.green += self.g
            self.i += 1
        pygame.draw.circle(self.root, (self.red, self.green, self.blue), (self.pos[0], self.pos[1]), self.rad - self.i)



line = Gradient_lines((0, 0), (200, 0), 200, (0, 1, 1), WIN)
circle = Gradient_circles((400, 200), 150, (1, 1, 1), WIN)
while True:
    line.draw()
    circle.draw()
    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()

