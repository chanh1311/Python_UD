import pygame, sys
from pygame.locals import *

pygame.init()
pygame.font.init()

DISPLAYSURF = pygame.display.set_mode((500,600))
pygame.display.set_caption("Hello world!")

total_secs = 0

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GRAY = (120,120, 120)
font = pygame.font.SysFont('consolas', 30)

while True:


	DISPLAYSURF.fill(GRAY)
	pygame.draw.rect(DISPLAYSURF, WHITE, (75, 75, 50, 50))
	pygame.draw.rect(DISPLAYSURF, WHITE, (175, 75, 50, 50))
	pygame.draw.rect(DISPLAYSURF, WHITE, (75, 200, 50, 50))
	pygame.draw.rect(DISPLAYSURF, WHITE, (175, 200, 50, 50))
	pygame.draw.rect(DISPLAYSURF, WHITE, (275, 75, 150, 50))
	pygame.draw.rect(DISPLAYSURF, WHITE, (275, 200, 150, 50))

	pygame.draw.circle(DISPLAYSURF,BLACK,(250, 400),75)
	pygame.draw.circle(DISPLAYSURF,WHITE,(250, 400),70)
	pygame.draw.circle(DISPLAYSURF,BLACK,(250, 400),5)

	pygame.draw.line(DISPLAYSURF, BLACK, (250, 400), (250, 335), 2)

	pygame.draw.rect(DISPLAYSURF, WHITE, (50, 500, 400, 50))
	pygame.draw.rect(DISPLAYSURF, BLACK, (50, 500, 400, 50),5)


	

	textSurface = font.render('START', True, BLACK)
	textSurface2 = font.render('RESET', True, BLACK)
	textSurface3 = font.render('+', True, BLACK)
	textSurface4 = font.render('-', True, BLACK)
	



	DISPLAYSURF.blit(textSurface, (300, 75))
	DISPLAYSURF.blit(textSurface2, (300, 200))

	DISPLAYSURF.blit(textSurface3, (90, 90))
	DISPLAYSURF.blit(textSurface3, (190, 90))

	DISPLAYSURF.blit(textSurface4, (90, 215))
	DISPLAYSURF.blit(textSurface4, (190, 215))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				mouse_x,mouse_y = pygame.mouse.get_pos()
				if mouse_x >= 175 and mouse_x <= 225:
					if mouse_y >= 75 and mouse_y <= 125:
						total_secs +=1
					elif mouse_y >= 200 and mouse_y <= 250:
						if total_secs >= 1:
							total_secs -=1
				elif mouse_x >= 75 and mouse_x <= 125: 
					if mouse_y >= 75 and mouse_y <= 125:
						total_secs +=60
					elif mouse_y >= 200 and mouse_y <= 250:
						if total_secs >= 60:
							total_secs -=60
						else:
							total_secs = 0
				elif mouse_x >= 275 and mouse_x <= 425: 
					if mouse_y >= 200 and mouse_y <= 250:
						total_secs = 0

	mins = int(total_secs / 60)
	secs = total_secs - mins * 60
	time_now = str(mins) + ":" + str(secs)

	textSurface = font.render(time_now, True, BLACK)
	DISPLAYSURF.blit(textSurface, (125, 150))
		

	
	pygame.display.update()

