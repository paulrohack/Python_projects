import pygame,sys
from time import sleep
import time
import tkinter
import random
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 750, 680
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
pygame.mixer.music.set_volume(0.3)
path = 'Pygame\\assets\\'
song = pygame.mixer.music.load(path + 'song.mp3')
pygame.mixer.music.play(-1)
#Load Icons
MUTE_PNG = pygame.image.load(path + 'mute.png')
HELP_PNG = pygame.image.load(path + 'help.png')
# Load images
RED_SPACE_SHIP = pygame.image.load(path +'pixel_ship_red_small.png')
GREEN_SPACE_SHIP = pygame.image.load(path + 'pixel_ship_green_small.png')
BLUE_SPACE_SHIP = pygame.image.load(path + 'pixel_ship_blue_small.png')
# Player player
YELLOW_SPACE_SHIP = pygame.image.load(path + 'pixel_ship_yellow.png')
# Lasers
RED_LASER = pygame.image.load(path + 'pixel_laser_red.png')
GREEN_LASER = pygame.image.load(path + 'pixel_laser_green.png')
BLUE_LASER = pygame.image.load(path + 'pixel_laser_blue.png')
YELLOW_LASER = pygame.image.load(path + 'pixel_laser_yellow.png')
# Background
BG = pygame.transform.scale(pygame.image.load(path + 'tryme.jpg'), (WIDTH, HEIGHT))
    
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)
class Ship:
    COOLDOWN = 30
    

    def __init__(self, x, y, health=500):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown(1)
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 5
                self.lasers.remove(laser)

    def cooldown(self,x):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += x

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()
class button():
    def __init__(self, color, x,y,width,height, text='' , image ='' ):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image = image

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        if self.text != '':
            font = pygame.font.SysFont('algerian', 20)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
            
    def icon_image(self,win):
        if self.image != '':
            win.blit(self.image, (self.x , self.y ))
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
class Player(Ship):
    def __init__(self, x, y, health=500):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        
        self.cooldown(1)
        
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)
                            
    def draw(self, window):
        super().draw(window)
        self.healthbar(window)
    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))

class Enemy(Ship):
    COLOR_MAP = {
                "red": (RED_SPACE_SHIP, RED_LASER),
                "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
                }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

mute = False
def MUTE():
    global mute
    if mute == True:
        pygame.mixer.music.play(-1)
        del mute
        mute = False
        
    else:

        pygame.mixer.music.stop()
        del mute
        mute = True

        
def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("algerian", 26)
    lost_font = pygame.font.SysFont("algerian", 40)
    enemies = []
    wave_length = 2
    enemy_vel = 2
    player_vel = 8
    laser_vel = 3
    laser = 8
    player = Player(325,500)
    
    clock = pygame.time.Clock()
    lost = False
    win = False
    lost_count = 0
    win_count = 0
   
    
    def redraw_window():
        WIN.blit(BG, (0,0))
        button_mute = button((255,255,255),10,47,10,47,image=MUTE_PNG)
        button_help = button((255,255,255),50,47,50,47,image=HELP_PNG)
        button_mute.icon_image(WIN)
        button_help.icon_image(WIN)
        
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 0, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 0, (255,255,255))
        title = main_font.render("__Space Shooter__", 0, (255,255,255))
        # border = main_font.render("----------------------------------------------------------------------------------------------", 0, (255,255,255))
        WIN.blit(lives_label, (10, 10))
        # WIN.blit(border, (0, 70))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        WIN.blit(title, (WIDTH/2 - title.get_width()/2, 10))
        
        for enemy in enemies:
            enemy.draw(WIN)
        player.draw(WIN)
        
        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
        if win:
            lost_label = lost_font.render("WINNER WINNER CHICKEN DINNER!!", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
            sleep(4)
            WIN.blit(BG , (0,0))
        pygame.display.update()
    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1
        if  level == 10:
            win = True
            win_count += 1
            main()
        if  level > 6:
            player.cooldown(2)      
        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue
        if len(enemies) == 0:
            level += 1
            level_up = pygame.mixer.Sound(path + 'orchestra.wav')
            level_up.set_volume(1)
            level_up.play()
            wave_length += 2
            for _ in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)
            pygame.display.update()
        for event in pygame.event.get():
            position = pygame.mouse.get_pos()
            button_mute = button((255,255,255),10,47,14,44,image=MUTE_PNG)
            button_help = button((255,255,255),50,47,50,47,image=HELP_PNG)
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_help.isOver(position): 
                    main_help()
                    sleep(6)
                if button_mute.isOver(position):
                    MUTE()
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 70: # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
            player.y += player_vel
        if keys[pygame.K_LEFT] and player.x - player_vel > 0: # left
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH: # right
            player.x += player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 70: # up
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()
            shot = pygame.mixer.Sound(path +'shot.wav')
            shot.set_volume(0.1)
            shot.play()
        pygame.display.update()
        def main_help():
            title_font = pygame.font.SysFont("algerian", 30)
            WIN.blit(BG, (0,0))
            title_label = title_font.render("   RIGHT = [right arrow]", 1, (225,225,225))
            WIN.blit(title_label,(10,40))
            title_label = title_font.render("   LEFT = [left arrow]", 1, (225,225,225))
            WIN.blit(title_label,(10,80))
            title_label = title_font.render("   UP = [up arrow]", 1, (225,225,225))
            WIN.blit(title_label,(10,120))
            title_label = title_font.render("   DOWN = [down arrow]", 1, (225,225,225))
            WIN.blit(title_label,(10,160))
            title_label = title_font.render("   SHOOT = [space]", 1, (225,225,225))
            WIN.blit(title_label,(10,200))
            title_label = title_font.render("           MADE BY PAUL SAMUEL :", 1, (225,225,225))
            WIN.blit(title_label,(10,300))

            pygame.display.update()
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)
            if random.randrange(0, 2*60) == 1:
                enemy.shoot()
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
        player.move_lasers(-laser, enemies )
        pygame.display.update()
def main_menu():
    title_font = pygame.font.SysFont("algerian", 40)
    run = True
    while run:
        WIN.blit(BG, (0,0))
        title_label = title_font.render("Tap enter to begin...", 1, (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                main()          
    pygame.quit()
main_menu()