import pygame
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Helvetica Neue", 30)
#variables
X_VEL = 1
Y_VEL = -2
X_PADDLE = 5

SCORE = 0
# ICON = ('assets\\joystick.png')

#window size
W =  1000
H =  700
#surface
pygame.display.set_caption("SQUASH BALL GAME ")
WIN = pygame.display.set_mode((W, H))
# pygame.display.set_icon(pygame.image.load(ICON))
black = (0,0,0)
white = (255,255,255)
green = (34,139,34)
red = (255,10,10)
#Ball
class Ball:
    def __init__(self, x, y, COLOR, RADIUS, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.COLOR = COLOR
        self.RADIUS = RADIUS
    def show(self,COLOR):
        pygame.draw.circle(WIN,self.COLOR,(self.x,self.y),self.RADIUS)

    def update(self):
        WIN.fill(black)
        ball.x += self.xv
        ball.y += self.yv
        if (ball.x  >= W - self.RADIUS):
            self.xv = -self.xv 
        if (ball.y >= H):
            pygame.quit()
        elif (ball.x  <= 0 + self.RADIUS):
            self.xv = -self.xv
        elif (ball.y  <= 0 + self.RADIUS):
            self.yv = -self.yv
        elif (ball.y == H-60 and ball.x>= paddle.x and ball.x <= paddle.x + paddle.sizex):
            self.yv = -self.yv 
            #self.xv += 1           
            global SCORE
            SCORE += 10            
        self.show(green)
#Paddle
class Paddle:
    def __init__(self, x, y, sizex, sizey, xv):
        self.x = x
        self.y = y
        self.sizex = sizex
        self.sizey = sizey
        self.xv = xv
    def show(self,COLOR):
        self.COLOR = COLOR
        pygame.draw.rect(WIN,self.COLOR,(self.x,self.y,self.sizex,self.sizey))
    def update(self):
        #Mouse controls
        '''if pygame.mouse.get_pressed()[0] and paddle.y >= 4 :
                                    paddle.x =  pygame.mouse.get_pos()[0] + self.yv'''
        #Key controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.x >= 4: # up
            paddle.x -= self.xv
        if keys[pygame.K_RIGHT] and paddle.x <= W-104 : # down
            paddle.x += self.xv
        self.show(red)

ball = Ball(W//4, H//2, green, 15, X_VEL, Y_VEL)
paddle = Paddle((W//2 - 100//2),(H-50),130,15,X_PADDLE)
ball.show(green)
paddle.show(red)

#Loop
while True:
    #print(SCORE)
    label = font.render(f"SCORE: {SCORE}", 0, white)
    ball.update()
    paddle.update()

    WIN.blit(label,(10,10))
    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()

