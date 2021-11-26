import pygame, sys

from pygame.math import enable_swizzling

W =  700
H =  600
square = pygame.image.load("H:\Assets\Square.png")
circle = pygame.transform.scale(pygame.image.load("H:\Assets\Circle.png"), (100, 100))
triangle = pygame.transform.scale(pygame.image.load("H:\Assets\Triangle.png"), (100, 100))
squarefrnd = pygame.image.load("H:\Assets\Squarefrnd.png")
circlefrnd = pygame.transform.scale(pygame.image.load("H:\Assets\Circlefrnd.png"), (100, 100))
trianglefrnd = pygame.transform.scale(pygame.image.load("H:\Assets\Trianglefrnd.png"), (100, 100))
bluecolor = '#5387ed'
WIN = pygame.display.set_mode((W, H))
s, c, t = 10, 10, 10
while True:
    pygame.time.Clock().tick(120)
    WIN.fill(bluecolor)
    WIN.blit(squarefrnd, (50, 50))
    WIN.blit(circlefrnd, (50, 250))
    WIN.blit(trianglefrnd, (50, 450))
    # WIN.blit(circle, (0, 200))
    # WIN.blit(square, (0, 0))
    # WIN.blit(triangle, (0, 400))
    
    keys = pygame.key.get_pressed()
    pygame.draw.rect(WIN, pygame.Color('red'), (0, 0, s, 20))
    if keys[pygame.K_q]: # up
        if s > 0 and s < W:
            WIN.blit(squarefrnd, (W//2 - 50, H//2 - 50))
            s -= 1
    else:
        s += 1
    pygame.draw.rect(WIN, pygame.Color('orange'), (0, 20, c, 20))
    if keys[pygame.K_w]: # up
        if c > 0 and c < W:  
            WIN.blit(circlefrnd, (W//2 - 50, H//2 - 50))
            c -= 1
    else:
        c += 1
    pygame.draw.rect(WIN, pygame.Color('pink'), (0, 40, t, 20))
    if keys[pygame.K_e]: # up
        if t > 0 and t < W:  
            WIN.blit(trianglefrnd, (W//2 - 50, H//2 - 50))
            t -= 1
    else:
        t += 1
    




    # if keys[pygame.K_RIGHT]: # down
    #     paddle.x += self.xv
    # self.show(red)
    # print(i)
    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()