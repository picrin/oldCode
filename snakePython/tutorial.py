import pygame, sys
pygame.init()
size = width, height = (800, 600)
screen = pygame.display.set_mode(size)
position = [400, 300]
speed = [1,1]
while True:
	queue = pygame.event.get()
	for event in queue:
		if event.type == pygame.QUIT:
			sys.exit()
	position[0] += speed[0]
	position[1] += speed[1]
	screen.fill((0,0,0))
	
	pygame.draw.circle(screen, (123,30,206), position, 10)
	
	pygame.display.update()

