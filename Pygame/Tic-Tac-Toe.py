import pygame
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Ariel", 70)
Sfont = pygame.font.SysFont("Ariel", 47)

#UI must be tweeked

W =  600
H =  600
rows = W//3
columns = H//3
o_image = pygame.image.load("assets\O.png")
x_image = pygame.image.load("assets\X.png")
WIN = pygame.display.set_mode((W, H))
WIN.fill('grey')
board = [   
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
    ]
winner = False

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
current_player = 'x'
turns = 0
moves_taken = []
run = True
while run:
    pygame.time.Clock().tick(60)
    # if play:
    if winner: 
        WIN.fill('grey')
        WIN.blit(font.render(f"WINNER: {current_player.upper()}", 10, pygame.Color('black')),(W//4,H//2))
        WIN.blit(Sfont.render(f"RIGHT MOUSE CLICK TO CONTINUE", 10, pygame.Color('black')),(0, H - 100))
        
        if pygame.mouse.get_pressed()[2]:
            run = False
    if turns > 8:
        WIN.fill('grey')
        WIN.blit(font.render(f"DRAW", 10, pygame.Color('black')),(W//4,H//2))
        WIN.blit(Sfont.render(f"RIGHT MOUSE CLICK TO CONTINUE", 10, pygame.Color('black')),(0, H - 100))

        if pygame.mouse.get_pressed()[2]:
            run = False       
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
                        if not winner:
                            if current_player == 'x':
                                WIN.blit(x_image, (x, y))
                                current_player = 'o'
                            else:
                                current_player = 'x'
                                WIN.blit(o_image, (x, y))
                        turns += 1

    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
