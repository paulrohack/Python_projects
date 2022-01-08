from numpy import sin, cos, pi, tan, arange, zeros
import pygame, sys

scale = 150
W =  int(scale*4*pi)
H =  1080
WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
xoff, yoff = W//2, H//2

xList = list(arange(0, 4*pi * scale, 1))
sin_yList = []
cos_yList = []
tan_yList = []

AMPLITUDE = 1
WAVE_LENGHT = 1
PHI = scale * pi/2 


pygame.draw.line(WIN, pygame.Color('white'), (0, yoff), (W, yoff), 1)
pygame.draw.line(WIN, pygame.Color('white'), (0, yoff - AMPLITUDE * scale), (W, yoff - AMPLITUDE * scale), 1)
pygame.draw.line(WIN, pygame.Color('white'), (0, yoff + AMPLITUDE * scale), (W, yoff + AMPLITUDE * scale), 1)

for i in range(9):
    if i % 2 != 0:
        pygame.draw.circle(WIN, pygame.Color('white'), (scale * i * pi/2, yoff), 6)
    pygame.draw.circle(WIN, pygame.Color('white'), (scale * i * pi, yoff), 6)

for x in xList:
    sin_yList.append(sin((1/(WAVE_LENGHT * scale)) * (x)) * AMPLITUDE * scale)
    # cos_yList.append(sin((1/(WAVE_LENGHT * scale)) * (PHI - x)) * AMPLITUDE * scale)
    # tan_yList.append(tan((1/(WAVE_LENGHT * scale)) * (x)) * AMPLITUDE * scale)

if sin_yList != []:
    for x, y in zip(xList, sin_yList):
        pygame.draw.circle(WIN, pygame.Color('#0e438c'), (x, y + yoff), 2)
        pygame.display.update()
if cos_yList != []:
    for x, y in zip(xList, cos_yList):
        pygame.draw.circle(WIN, pygame.Color('#918313'), (x, y + yoff), 2)
        pygame.display.update()
if tan_yList != []:
    for x, y in zip(xList, tan_yList):
        pygame.draw.circle(WIN, pygame.Color('#278537'), (x, y + yoff), 2)
        pygame.display.update()

while True:
    for events in pygame.event.get():
        if events.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()
