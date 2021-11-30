import pygame, time
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Ariel", 70)
Sfont = pygame.font.SysFont("Ariel", 47)

#UI must be tweeked

W =  600
H =  600
rows = W//3
columns = H//3
o_image = pygame.image.load("H:\\Python\\assets\\O.png")
x_image = pygame.image.load("H:\\Python\\assets\\X.png")
WIN = pygame.display.set_mode((W, H))
WIN.fill('#5c86a6')
board = [   
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
    ]
winner = False


def end_screen(player):
    if player != None:
        WIN.fill('grey')
        WIN.blit(font.render(f"'{current_player.upper()}' IS THE WINNER!", 0, pygame.Color("black")), (70, H/2 - 35))
        WIN.blit(Sfont.render(f"RIGHT MOUSE CLICK to close", 1, pygame.Color("black")), (55, H - 30))
    else:
        WIN.fill('grey')
        WIN.blit(font.render(f"DRAW!", 0, pygame.Color("black")), (W/2 - 80, H/2 - 35))
        WIN.blit(Sfont.render(f"RIGHT MOUSE CLICK to close", 1, pygame.Color("black")), (55, H - 30))



def check(board):
    for row in range(3):
        if (board[row][0]) == (board[row][1]) == (board[row][2]) != "-":
            
            return True

    for col in range(3):
        if (board[0][col]) == (board[1][col]) == (board[2][col]) != "-":
            return True

    if (board[0][0]) == (board[1][1]) == (board[2][2]) != "-":
        return True
    if (board[0][2]) == (board[1][1]) == (board[2][0]) != "-":
        return True   
for x in range(0, W, rows):
    for y in range(0, H, columns):
        pygame.draw.circle(WIN, pygame.Color("black"), (x + rows//2, y + columns//2), 5, 1)
current_player = 'x'
turns = 0
moves_taken = []
run = True
while run:
    pygame.time.Clock().tick(60)
    if winner: 
        end_screen(current_player)
        # time.sleep(1)
        # run = False  
    else:
        if turns > 8:
            end_screen(None)

            # run = False  
    if not winner:
        for x in range(0, W, rows):
            for y in range(0, H, columns):
                pos = pygame.mouse.get_pos()
                celly, cellx = x//columns, y//rows
                if pygame.mouse.get_pressed()[0]:
                    if pos[0] > x and pos[0] < x + columns and pos[1] > y and pos[1] < y + rows:
                        if (cellx, celly) not in moves_taken:
                            moves_taken.append((cellx, celly))
                            board[cellx][celly] = current_player
                            winner = check(board)
                        
                            if current_player == 'x':
                                WIN.blit(x_image, (x, y))
                                if not winner:
                                    current_player = 'o'
                            else:
                                WIN.blit(o_image, (x, y))
                                if not winner: current_player = 'x'
                            
                            turns += 1
                            pygame.draw.rect(WIN, pygame.Color("#3f414d"), (x, y, rows, columns), 10)

    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
