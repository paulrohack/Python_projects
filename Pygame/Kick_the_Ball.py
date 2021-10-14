import pygame
pygame.init()
W =  900
H =  600
WIN = pygame.display.set_mode((W, H))
bg = pygame.image.load("Pygame\\assets\Background_football.png")

goal = pygame.image.load("Pygame\\assets\Goal_Football.png").convert_alpha()
goal = pygame.transform.scale(goal, (300,300))
# goal = pygame.transform.rotate(goal, -90)

player = pygame.image.load("Pygame\\assets\Player-Football.png").convert_alpha()
player = pygame.transform.scale(player, (100,100))
goalkeeper = pygame.image.load("Pygame\\assets\GoalKeeper-Football.png").convert_alpha()
goalkeeper = pygame.transform.scale(goalkeeper, (200,200))



goal_x= W//3
goal_offset = 10
player_offset = 30
goalkeeper_x = goal_offset + player_offset
speed = 0.5
while True:
    WIN.blit(bg, (0, 0))
    WIN.blit(goal, (-10, H//2 - 200))
    WIN.blit(goal, (300, H//2 - 200))
    WIN.blit(goal, (600 + goal_offset, H//2 - 200))

    WIN.blit(player, (W//2 - 50, H-100))
    WIN.blit(goalkeeper, (goalkeeper_x, H//4 + 50))


    goalkeeper_x += speed
    if goalkeeper_x > W - 250 or goalkeeper_x < goal_offset + player_offset:
        speed *= -1
        
    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()