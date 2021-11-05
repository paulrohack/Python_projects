import pygame, math
pygame.init()
W =  800
H =  600
WIN = pygame.display.set_mode((W, H))
PLAYER = pygame.image.load('assets\pixel_ship_yellow.png')
FLAME = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('assets\Fire.png'), (80, 50)), 180)

class Car:
    def __init__(self, x, y, car_w, car_h, vel, r_vel, player_image, effects):
        self.x = x
        self.y = y
        self.car_w = car_w
        self.car_h = car_h
        self.vel = vel
        self.r_vel = r_vel
        self.player_image = player_image
        self.effects = effects
        self.flame = self.effects
        self.car = pygame.transform.scale(self.player_image, (self.car_w, self.car_h))
        self.angle = math.radians(0)
        
    def draw(self, win):
        self.fy = self.y + self.car_h
        self.fx = self.x
        win.blit(self.car, (self.x, self.y))
        win.blit(self.flame, (self.fx, self.fy))
    def move(self):
        keys = pygame.key.get_pressed()
        # pygame.draw.line(WIN, pygame.Color('red') , (self.x + self.car_w//2 , self.y),(self.x + self.car_w//2 - math.sin(self.angle) * 50, self.y + math.cos(self.angle) * 50))
        if keys[pygame.K_LEFT]: 
            self.angle -= 0.1
        if keys[pygame.K_RIGHT]: 
            self.angle += 0.1
        if keys[pygame.K_DOWN]:
            self.x += -math.sin(self.angle) * self.vel
            self.y += math.cos(self.angle) * self.vel
        if keys[pygame.K_UP]:
            self.x -= -math.sin(self.angle) * self.vel
            self.y -= math.cos(self.angle) * self.vel
        self.car = pygame.transform.rotate(self.player_image, -math.degrees(self.angle))
        self.flame = pygame.transform.rotate(self.effects, -math.degrees(self.angle))

        
car_width, car_height= 70, 70
car = Car(W/2 - car_width/2, H - car_height - 20, car_width, car_height, 4, 4, PLAYER, FLAME)
run = True
while run:
    pygame.time.Clock().tick(100)
    WIN.fill(0)
    car.draw(WIN)  
    # WIN.blit(FLAME, (car.x, car.y + car.car_h))
    car.move()
    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
# exit()