from MyModules.NumberSystem_conversion import *
import pygame, datetime
pygame.font.init()
W =  600
H =  300
WIN = pygame.display.set_mode((W, H))
pygame.display.set_caption("Binary Clock")
cy = H//4
font = pygame.font.SysFont("algerian", 30)

while True:
    HOUR    = datetime.datetime.now().hour
    MINUTE  = datetime.datetime.now().minute
    SECONDS = datetime.datetime.now().second
    pygame.time.Clock().tick(60)
    hours = decimal_to_binary(HOUR)
    minutes = decimal_to_binary(MINUTE)
    seconds = decimal_to_binary(SECONDS)
    l = 5

    hours = list(hours)
    minutes = list(minutes)
    seconds = list(seconds)

    minu = len(minutes)
    sec = len(seconds)
    hrs = len(hours)
    if hrs < 6:
        while hrs != 6:
            hours.insert(0, '0')
            hrs = len(hours)
    if minu < 6:
        while minu != 6:
            minutes.insert(0, '0')
            minu = len(minutes)
    if sec < 6:
        while sec != 6:
            seconds.insert(0, '0')
            sec = len(seconds)

    for x in range(0, W, (W//6)):
        for y in range(0, H, cy):
            if y//(cy) == 0:#Binary Numbers
                label = (2 ** l)
                LABEL = font.render(f"{label}", 2, (255,255,255))
                WIN.blit(LABEL, (x + (((W//6)//2)-15), (cy//2 - 15)))   
                rect = pygame.Rect(x, y, (W//6), cy - 5)
                pygame.draw.rect(WIN, 'yellow', rect, 3)
                l -= 1
            if y//(cy) == 1:#hours
                if hours[x//(W//len(hours))] == '1':
                    color = 'yellow'
                else:
                    color = 'black'
                rect = pygame.Rect(x + 2, y, (W//len(hours)) - 2, cy - 5)
                pygame.draw.rect(WIN, color, rect)
            if y//(cy) == 2:#minutes
                if minutes[x//(W//len(minutes))] == '1':
                    color = 'yellow'
                else:
                    color = 'black'
                rect = pygame.Rect(x + 2, y, (W//len(minutes)) - 2, cy - 5)
                pygame.draw.rect(WIN, color, rect)

            if y//(cy) == 3:#seconds
                if seconds[x//(W//len(seconds))] == '1':
                    color = 'yellow'
                else:
                    color = 'black'
                rect = pygame.Rect(x + 2, y, (W//len(seconds)) - 2, cy)
                pygame.draw.rect(WIN, color, rect)
    pygame.display.update()

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()





