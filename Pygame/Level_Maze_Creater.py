import pygame
import math

WIDTH, HEIGHT = 600, 600
cube_s = 50


WIN = pygame.display.set_mode((WIDTH, HEIGHT))

player_img = pygame.image.load('assets\\Player.png').convert_alpha()
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
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
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
        # img = pygame.transform.rotate(player_img, -pa * 180/math.pi )
        # WIN.blit(img, (self.x, self.y))
        pygame.draw.circle(WIN, (255, 100, 50), (self.x, self.y), 3)
        pygame.draw.line(WIN, (0, 255, 0), (self.x , self.y),(self.x - math.sin(pa) * 50, self.y + math.cos(pa) * 50), 3)
        pygame.draw.line(WIN, (255,255, 10), (self.x , self.y),((self.x - math.sin(pa + math.pi/6) * 50), (self.y + math.cos(pa  + math.pi/6) * 50)), 5)
        pygame.draw.line(WIN, (255,255, 10), (self.x , self.y),((self.x - math.sin(pa - math.pi/6) * 50), (self.y + math.cos(pa  - math.pi/6) * 50)), 5)

    def cast_rays(self):
        # define left most angle of FOV
        start_angle = pa - math.pi/6
        
        # loop over casted rays
        for ray in range(120):
            # cast ray step by step
            for depth in range(WIDTH):
                # get ray target coordinates
                target_x = self.x - math.sin(start_angle) * depth
                target_y = self.y + math.cos(start_angle) * depth
                
                # covert target X, Y coordinate to map col, row
                col = int(target_x / WIDTH//12)
                row = int(target_y / WIDTH//12)
    
            start_angle += (math.pi/3) /  120    
            


man = player(200, 200, 0.1)
pdx = math.cos(pa) * s
pdy = math.sin(pa) * s
while True:
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]: 
        pa -= 0.1
        # player_img = pygame.transform.rotate(player_img, player_angle)
    if keys[pygame.K_RIGHT]: 
        pa += 0.1
        # player_img = pygame.transform.rotate(player_img, player_angle)
    if keys[pygame.K_UP]:
        man.x += -math.sin(pa) * 5
        man.y += math.cos(pa) * 5
    if keys[pygame.K_DOWN]:
        man.x -= -math.sin(pa) * 5
        man.y -= math.cos(pa) * 5

        
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
    WIN.fill('black')
    
    
    mp_()
    man.draw()
    man.cast_rays()
    pygame.time.Clock().tick(60)
