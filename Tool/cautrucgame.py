import pygame, sys
from pygame.locals import *



BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GRAY = (120,120, 120)

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 600))
pygame.display.set_caption('Hello world!')
font = pygame.font.SysFont('consolas', 30)









while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                print(mouse_x)
                print(mouse_y)
            elif event.button == 3:
                mouse_xp,mouse_yp = pygame.mouse.get_pos()
                print("P: " + str(mouse_xp))
                print("P: "+ str(mouse_yp))    
                
    # DISPLAYSURF.fill((120, 120, 120))


    # mins = int(total_secs / 60)
    # secs = total_secs - mins * 60
    # time_now = str(mins) + ":" + str(secs)

    
    # textSurface = font.render(time_now, True, WHITE)
    # DISPLAYSURF.blit(textSurface, (300, 75))
    # pygame.draw.rect(DISPLAYSURF, (255, 255, 0), (100, 80, 150, 50))

    pygame.display.update()