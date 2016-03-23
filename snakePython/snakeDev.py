import sys, pygame, collections, random
from pygame.locals import *

class Snake(object):
	def __init__(self, length, keyset, position, direction, segment = "segment.bmp"):
		self.direction = direction
		self.keyset = keyset
		self.segment = pygame.image.load(segment)
		self.rect = pygame.Rect(0,0,length,length)
		self.length = self.rect[-1]
		self.segmentsRect = collections.deque([self.rect.copy() for i in range(length)])
		self.spread(position, self.direction, self.length)
	def spread(self, position, direction, length):
		by = position
		increase = [i*length for i in direction]
		for rectangle in self.segmentsRect:
			rectangle.move_ip(by)
			by[0] += increase[0]
			by[1] += increase[1]
	def keyStroke(self,eventKey):
		if eventKey in self.keyset:
			self.direction = self.keyset[eventKey]
	def move(self):
		step = [element*self.length for element in self.direction]
		self.segmentsRect.popleft()
		last = self.segmentsRect[-1]
		newRect = last.copy()
		self.segmentsRect.append(newRect.move(step))
	def giveSegment(self):
		return self.segment
	def giveRects(self):
		return self.segmentsRect


pygame.init()
size = width, height = 800, 600
black = 0, 0, 0
screen = pygame.display.set_mode(size)
down = [0,1]
up = [0,-1]
right = [1,0]
left = [-1,0]

snake1 = Snake(8, keyset = {pygame.K_UP : up, pygame.K_DOWN : down, pygame.K_RIGHT : right, pygame.K_LEFT : left}, position = [width,height/2], direction = left, segment = "segment.bmp")
snake2 = Snake(8, keyset = {pygame.K_w : up, pygame.K_s : down, pygame.K_d : right, pygame.K_a : left}, position = [0,height/2], direction = right, segment = "segment2.bmp")
snake3 = Snake(8, keyset = {pygame.K_KP8 : up, pygame.K_KP5 : down, pygame.K_KP6 : right, pygame.K_KP4 : left}, position = [width/2,0], direction = down, segment = "segment.bmp")
snakes = [snake1,snake2, snake3]

while True:
	pygame.time.wait(80)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			for snake in snakes:
				snake.keyStroke(event.key)
#	if rects[-1].left < 0 or rects[-1].right > width:
#		direction[0] = -direction[0]
#	if rects[-1].top < 0 or rects[-1].bottom > height:
#		direction[1] = -direction[1]
	screen.fill(black)
	for snake in snakes:
		snake.move()
		for rect in snake.giveRects():
			screen.blit(snake.giveSegment(), rect)
	pygame.display.flip()
