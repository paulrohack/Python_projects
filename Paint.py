import pygame
pygame.font.init()
font = pygame.font.SysFont("Helvetica Neue", 30)

W =  600
H =  600
paint_size = 7
colors = ['black','gray','blue','red','green','yellow','cyan','brown','pink', 'white', 'orange']
buttonx, buttony = 100, 60
n = 0
pygame.display.set_caption("PY-PAINT")
WIN = pygame.display.set_mode((W, H))

tool = ""
Plus = font.render("SIZE++", 0, pygame.Color('black'))
Minus = font.render("SIZE--", 0, pygame.Color('black'))
eraser_text = font.render("ERASER", 0, pygame.Color('black'))



eraser = 'white'
if eraser in colors:
    colors.remove(eraser)
    # print(colors)
current_color = colors[0]
next_color = colors[1]
erase = False

WIN.fill(pygame.Color(eraser))
px, py = 0, 0
pencil, brush = True, False
# pencil, brush = False, True
while True:
    pygame.time.Clock().tick(500)
    pos = pygame.mouse.get_pos()
    Tool_used = font.render(tool, 0, pygame.Color('black'))     

    # pygame.draw.line(WIN, pygame.Color('black'), (px, py), (pos), 3
    pygame.draw.rect(WIN, current_color, (0, H - buttony, buttonx, buttony))
    pygame.draw.rect(WIN, next_color, (0, H - buttony, buttonx, buttony), width=5)

    pygame.draw.rect(WIN, pygame.Color(eraser), (buttonx, H - buttony, buttonx, buttony))
    pygame.draw.rect(WIN, pygame.Color('black'), (buttonx , H - buttony, buttonx, buttony), width=5)
    WIN.blit(eraser_text, (buttonx + buttonx/10 , H - buttony + buttony/3))

    pygame.draw.rect(WIN, pygame.Color('grey'), (buttonx * 2 , H - buttony, buttonx, buttony))
    pygame.draw.rect(WIN, pygame.Color('black'), ((buttonx*2), H - buttony, buttonx, buttony), width=5)
    WIN.blit(Plus, ((buttonx*2) + buttonx/10 , H - buttony + buttony/3))



    pygame.draw.rect(WIN, pygame.Color('grey'), (buttonx * 3 , H - buttony, buttonx, buttony))
    pygame.draw.rect(WIN, pygame.Color('black'), ((buttonx*3), H - buttony, buttonx, buttony), width=5)
    WIN.blit(Minus, ((buttonx*3) + buttonx/10 , H - buttony + buttony/3))


    pygame.draw.rect(WIN, pygame.Color('grey'), (buttonx * 4 , H - buttony, buttonx, buttony))
    pygame.draw.rect(WIN, pygame.Color('black'), ((buttonx*4), H - buttony, buttonx, buttony), width=5)
    
    WIN.fill(pygame.Color(eraser), (buttonx * 5, H - buttony, buttonx, buttony))
    pygame.draw.rect(WIN, pygame.Color('black'), ((buttonx*5), H - buttony, buttonx, buttony), width=5)

    WIN.blit(Tool_used, ((buttonx*4) + buttonx/10 , H - buttony + buttony/3))
    if pencil:
        tool = "PENCIL"
        pygame.draw.line(WIN, pygame.Color('black'), (((W - buttonx) + buttonx/4), (H - (buttony/2))), (((W - buttonx) + buttonx/4 + buttonx/2), (H - (buttony/2))), paint_size)
    else:
        tool = "BRUSH"
        pygame.draw.circle(WIN, pygame.Color('black'), (W - (buttonx/2), (H - (buttony/2))), paint_size)





    if pencil:
        if pygame.mouse.get_pressed()[0] and pos[1] < H - (buttony - 5):
            if not erase:
                pygame.draw.line(WIN, current_color, (px, py), (pos), paint_size)
                px, py = pos
            else:
                pygame.draw.circle(WIN, pygame.Color(eraser), pos, paint_size)
        else:
            px, py = pos
    elif brush:
        if pygame.mouse.get_pressed()[0] and pos[1] < H - (buttony - 5):
            if not erase:
                pygame.draw.circle(WIN, current_color, pos, paint_size)
            else:
                pygame.draw.circle(WIN, pygame.Color(eraser), pos, paint_size)

    pygame.display.update()
    
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
        elif events.type == pygame.MOUSEBUTTONDOWN:
            if pos[0] > 0 and pos[0] < buttonx and pos[1] > H - buttony and pos[1] < H:
                if n != len(colors)-1:
                    if not erase:
                        n += 1
                else:
                    n = 0
                erase = False
            if pos[0] > buttonx and pos[0] < 2 * buttonx and pos[1] > H - buttony and pos[1] < H:
                erase = True
            if pos[0] > 4*buttonx and pos[0] < 5 * buttonx and pos[1] > H - buttony and pos[1] < H:
                if brush:
                    brush = False
                    pencil = True
                elif pencil:
                    brush = True
                    pencil = False
                
            if paint_size < 20:
                if pos[0] > 2*buttonx and pos[0] < 3 * buttonx and pos[1] > H - buttony and pos[1] < H:
                    paint_size += 2
            if paint_size > 6:
                if pos[0] > 3*buttonx and pos[0] < 4 * buttonx and pos[1] > H - buttony and pos[1] < H:
                    paint_size -= 2
            current_color = colors[n]
            next_color = colors[n - 1]




