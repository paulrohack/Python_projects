import pygame
import math

WIDTH, HEIGHT = 600, 600
cube_s = 50


WIN = pygame.display.set_mode((WIDTH, HEIGHT))

player_img = pygame.image.load('Pygame\\assets\\Player.png').convert_alpha()
player_img = pygame.transform.scale(player_img, (50,50))




pa = -math.pi/2
pdx = 0
pdy = 0
s = 5
map_ = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        ]

def mp_():
    for x in range(0, WIDTH, cube_s):
        for y in range(0, HEIGHT, cube_s):
            if (map_[y//cube_s][x//cube_s] == 1):
                color = 'black'    
            elif (map_[y//cube_s][x//cube_s] == 0):
                color = 'white'
            else:
                color = 'brown'
            rect = pygame.Rect(x + 1, y + 1, cube_s - 1, cube_s - 1)
            pygame.draw.rect(WIN, color, rect)
            rect = pygame.Rect(x, y, cube_s, cube_s)
            pygame.draw.rect(WIN, 'white', rect, 1)

class player:
    def __init__(self, x, y, a):
        self.x = x
        self.y = y
        self.a = a
    def draw(self):
        img = pygame.transform.rotate(player_img, -pa * 180/math.pi )
        WIN.blit(img, (self.x, self.y))
    def check(self):
        x = 50 * round(self.x/50)
        y = 50 * round(self.y/50)
        rect = pygame.Rect(x, y, cube_s, cube_s)
        pygame.draw.rect(WIN, 'yellow', rect)
        try:
            if (map_[y//50][x//50]) == 1:
                self.x, self.y = 200, 200
            elif (map_[y//50][x//50]) == 2:
                pygame.quit()            
        except:
            pass
            
            


man = player(200, 200, 0.1)
pdx = math.cos(pa) * s
pdy = math.sin(pa) * s
while True:
    
    keys = pygame.key.get_pressed()
    
    man.y += pdy
    man.x += pdx
    if keys[pygame.K_s]:
        man.y -= pdy
        man.x -= pdx
    if keys[pygame.K_a]: 
        pa -= man.a
        if pa < 0:
           pa += 2*math.pi
        pdx = math.cos(pa) * s
        pdy = math.sin(pa) * s
    if keys[pygame.K_d]:
        pa += man.a
        if pa > 2*math.pi:
           pa -= 2*math.pi
        pdx = math.cos(pa) * s
        pdy = math.sin(pa) * s
        
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
    WIN.fill('black')
    
    
    mp_()
    man.check()

    man.draw()
    pygame.time.Clock().tick(60)
