from numpy import sin, cos, pi, tan, arange, zeros
import pygame, sys
W =  600
H =  600
WIN = pygame.display.set_mode((W, H))
i = 0
wave = []
def circle(radius, time, s = 1):
    x = radius * 4/(pi) * cos(time) + 200
    y = radius * 4/(pi) * sin(time) + 300
    pygame.draw.circle(WIN, pygame.Color("White"), (x, y), s)
l = 1
px, py, x, y = 0, 0, 0, 0
while True:
    x, y = 0, 0
    pygame.time.Clock().tick(60)

    WIN.fill(pygame.Color('Black'))
    radius = 100

    for t in range(360):
        circle(radius, t, 1)

    for z in range(0, 5):
        l = z * 2 + 1
        r = radius * 4/(l*pi)
        px, py = x, y
        x += r * cos(l*i) 
        y += r * sin(l*i)
        pygame.draw.line(WIN, pygame.Color('light blue'), (px + 200, py + 300), (x + 200, y + 300), 3)
        pygame.draw.circle(WIN, pygame.Color('light yellow'), (x + 200, y + 300), 3)
        pos = (x + 200, y + 300)
    wave.insert(0, pos[1] - 300)

    pygame.draw.line(WIN, pygame.Color('light blue'), pos, (400, 300 + wave[0]), 2)

    for n in range(1, len(wave)):
        pygame.draw.circle(WIN, pygame.Color('pink'), (n + 400, 300+ wave[n]), 1)
        pygame.draw.line(WIN, pygame.Color('light blue'), (n + 400, 300+ wave[n-1]), (n + 400, 300+ wave[n]))

    i += 0.05

    if len(wave) > 200: wave.pop()

    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
