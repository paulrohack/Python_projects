import pygame, sys, numpy as np
W =  600
H =  600
WIN = pygame.display.set_mode((W, H))
angle = 0
radius = 100
xoff, yoff = W//2, H//2
while True:
    WIN.fill(25)
    pygame.time.Clock().tick(60)


    x, y = radius * np.cos(angle), radius * np.sin(angle)

    pygame.draw.line(WIN, pygame.Color("light blue"), (xoff, yoff), (x + xoff, y + yoff), 1) #radius
    pygame.draw.line(WIN, pygame.Color("pink"), (x + xoff, y + yoff), (x + xoff, 10), 3) #x-line
    pygame.draw.line(WIN, pygame.Color("pink"), (x + xoff, y + yoff), (W-30, y + yoff), 3) #y-line
    pygame.draw.circle(WIN, pygame.Color("white"), (x + xoff, y + yoff), 20) # ball
    pygame.draw.circle(WIN, pygame.Color("green"), (xoff, yoff), radius, 1) #path made by the ball
    pygame.draw.rect(WIN, pygame.Color('orange'), (xoff - radius, 10, radius + x, 30)) #linear x
    pygame.draw.rect(WIN, pygame.Color('red'), (W-40, yoff - radius, 30,  radius + y)) #linear y
    pygame.draw.rect(WIN, pygame.Color("Yellow"), (xoff - radius, 10, radius + x, 30), 2) #borderx
    pygame.draw.rect(WIN, pygame.Color("Yellow"), (W-40, yoff - radius, 30,  radius + y), 2) #bordery 
    pygame.display.update()
    angle += 0.1
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()