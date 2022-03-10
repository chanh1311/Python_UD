import pygame, sys
from pygame.locals import *
import time
import math 
clock = pygame.time.Clock()
pygame.init()
pygame.font.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("tick.wav")
sound1 = pygame.mixer.Sound("timeout.wav")




DISPLAYSURF = pygame.display.set_mode((500,600))
pygame.display.set_caption("Hello world!")

TAMO = (250, 400)
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GRAY = (120,120, 120)

def status_now(start):
	if start:
		status = "TRẠNG THÁI: ĐANG CHẠY..."
	else:
		status = "TRẠNG THÁI: DỪNG!"
	return status


Rs = 400 - 335 #(Y(o) - Y(a))
Rp = 400 - 350 #(Y(o) - Y(a))


font = pygame.font.SysFont('consolas', 30)
font1 = pygame.font.SysFont('consolas', 15)
total_secs = 0
start = 0
status = status_now(start)

total = 0
tam = 0

#Vòng lặp chính game
while True:
	clock.tick(60)
	DISPLAYSURF.fill(GRAY)
	#Hình chữ nhật
	pygame.draw.rect(DISPLAYSURF, WHITE, (75, 75, 50, 50))
	pygame.draw.rect(DISPLAYSURF, WHITE, (175, 75, 50, 50))
	pygame.draw.rect(DISPLAYSURF, WHITE, (75, 200, 50, 50))
	pygame.draw.rect(DISPLAYSURF, WHITE, (175, 200, 50, 50))
	pygame.draw.rect(DISPLAYSURF, WHITE, (275, 75, 150, 50))
	pygame.draw.rect(DISPLAYSURF, WHITE, (275, 200, 150, 50))
	#Hình tròn
	pygame.draw.circle(DISPLAYSURF,BLACK,(250, 400),75)
	pygame.draw.circle(DISPLAYSURF,WHITE,(250, 400),70)
	pygame.draw.circle(DISPLAYSURF,BLACK,(250, 400),5)

	#Hình chữ nhật cuối
	pygame.draw.rect(DISPLAYSURF, WHITE, (50, 500, 400, 50))
	pygame.draw.rect(DISPLAYSURF, BLACK, (50, 500, 400, 50),5)

# Vòng lặp sự kiện
	for event in pygame.event.get():
		mouse_x,mouse_y = pygame.mouse.get_pos()
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:    #click chuột trái#     
				if mouse_x >= 175 and mouse_x <= 225 and start == 0: #cột 1#
					if mouse_y >= 75 and mouse_y <= 125: #dòng 1#
						total_secs +=1 					#tăng 1#
					elif mouse_y >= 200 and mouse_y <= 250:#dòng 2#
						if total_secs >= 1:				#Nếu lớn hơn 1 mới được giảm 1#
							total_secs -=1
				elif mouse_x >= 75 and mouse_x <= 125 and start == 0:  #côt 2#
					if mouse_y >= 75 and mouse_y <= 125:				#dòng 1#
						total_secs +=60 								#tăng 60#
					elif mouse_y >= 200 and mouse_y <= 250:				
						if total_secs >= 60:							#dòng 2 nếu lớn hơn 60 thì giảm 60#
							total_secs -=60
						else:
							total_secs = 0 								#nhỏ hơn 60 thì trở về 0#
				elif mouse_x >= 275 and mouse_x <= 425 and start == 0: #côt 3#
					if mouse_y >= 200 and mouse_y <= 250:				#Reset#
						total_secs = 0
						start = 0
					elif mouse_y >= 75 and mouse_y <= 125:				#Start#
						start = 1
			elif event.button == 3 and start == 1:  			#click phải#							   	#Lấy tđ#       												
				if mouse_x >= 275 and mouse_x <= 425 and mouse_y >= 75 and mouse_y <= 125:
						start = 0 

#Khi trạng thái bắt đầu thì thời gian giảm dần 1
	if start:
		#Nếu thời gian lớn hơn 0 thì thời gian giảm 1 đơn vị
		if total_secs > 0:
			sound.play()
			if tam == 0:
				total = total_secs
				tam = 1
			total_secs -= 1
			time.sleep(1)                 									
	#Khi thời gian bằng 0 thì trạng thái dừng
		else: 
			sound1.play()
			start = 0
	else:
		tam = 0
	#Trạng thái
	status = status_now(start)		
		

#Tính thời gian bằng số giây
	mins = int(total_secs / 60)
	secs = total_secs - mins * 60
	time_now = str(mins) + ":" + str(secs) 
	#Kim giây#
	A = 6 * (3.141592654/180) * secs 
	Xa = 250 + round((math.sin(A) * Rs))
	Ya = 400 - round((math.cos(A) * Rs))
	#Kim phút#
	B = 6 * (3.141592654/180) * mins
	Xb = 250 + round((math.sin(B) * Rp))
	Yb = 400 - round((math.cos(B) * Rp))

#Kim fast#

# tạo suface(nút bấm)
	if start:
		textSurface = font.render('STOP', True, RED)
	else:
		textSurface = font.render('START', True, GREEN)

	#Tạo các nút
	textSurface2 = font.render('RESET', True, BLACK)
	textSurface3 = font.render('+', True, BLACK)
	textSurface4 = font.render('-', True, BLACK)

	#Vẽ suface lên một suface khác
	DISPLAYSURF.blit(textSurface, (300, 75))
	DISPLAYSURF.blit(textSurface2, (300, 200))

	DISPLAYSURF.blit(textSurface3, (90, 90))
	DISPLAYSURF.blit(textSurface3, (190, 90))

	DISPLAYSURF.blit(textSurface4, (90, 215))
	DISPLAYSURF.blit(textSurface4, (190, 215))



#Hiển thị trạng thái, thời gian lên màn hình
	textSurface = font1.render(status, True, RED)
	DISPLAYSURF.blit(textSurface, (275, 150))	

	textSurface = font.render(time_now, True, BLACK)
	DISPLAYSURF.blit(textSurface, (125, 150))

#Hiển thị kim đồng hồ
	pygame.draw.line(DISPLAYSURF, BLACK, TAMO, (Xb, Yb), 3)
	pygame.draw.line(DISPLAYSURF, RED, TAMO, (Xa, Ya), 3)


#Hình chữ nhật đang chạy
	if not start:
		pygame.draw.rect(DISPLAYSURF,RED, (50, 500,400,50))
	else:
		pygame.draw.rect(DISPLAYSURF,RED, (50, 500,int(400 * (total_secs/total)), 50))

	
	pygame.display.flip()

