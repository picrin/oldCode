import sys, pygame, collections, random, numpy
from pygame.locals import *
screenColour = (255,255,255,)
screenColour = (0,0,0,)
class Snake(object):
	def __init__(self, length, wheel, size, keyset, position, direction):
		self.wheel = wheel
		self.direction = direction
		self.keyset = keyset
		self.rect = pygame.Rect((0,0,), (size, size,))
		self.surface = pygame.Surface((size,size,))
		self.blackSurface = pygame.Surface((size,size,))
		self.blackSurface.fill(screenColour)
		self.length = self.rect[-1]
		self.segmentsRect = collections.deque([self.rect.copy() for i in range(length)])
		self.spread(position, self.direction, self.length)
		self.toBlit = []
	def spread(self, position, direction, length):
		by = position
		increase = [i*length for i in direction]
		for rectangle in self.segmentsRect:
			rectangle.move_ip(by)
			by[0] += increase[0]
			by[1] += increase[1]
	def keyStroke(self,eventKey):
		if eventKey in self.keyset:
			newDirection = self.keyset[eventKey]
			if not([coordinate * (-1) for coordinate in newDirection] ==  self.direction): # unless snake is about to be moved in reverse direction
				self.direction = self.keyset[eventKey]
		
	def move(self, dirtyRects, collisions):
		step = [element*self.length for element in self.direction]
		popped = self.segmentsRect.popleft()
		last = self.segmentsRect[-1]
		newRect = last.copy()
		#print newRect[:2]
		if tuple(newRect[:2]) in collisions:
			raise Exception("Game Over")
		self.segmentsRect.append(newRect.move(step))
		pygame.surfarray.blit_array(self.surface, self.giveSegment())
		dirtyRects.append((self.surface, newRect,))
		dirtyRects.append((self.blackSurface, popped,))
	def giveSegment(self):
		return self.wheel.next()
	def giveRects(self):
		return self.segmentsRect

class Rainbow(object):
	def __init__(self, frameRate, sv, length, reverse = 0):
		self.reverse = reverse
		self.frameRate = frameRate
		mysurface = pygame.Surface((length,length,))
		self.frames = []
		for frameNumber in range(frameRate):
			nextFrame = self.generateFrame(frameNumber, self.reverse, sv, length)
			self.frames.append(nextFrame)
			self.reverse = not self.reverse
	def generateFrame(self, odcien, reverse, sv, length):
		arrayFrame = numpy.ndarray((length,length,3), dtype = int)
		for x in range(length):
			for y in range(length):
				if reverse:
					diagonal = (length - 1) - x + y
				else:
					diagonal = x + y
				v = sv[1]
				s = sv[0]
				if diagonal <= length - 1:
					v = float(diagonal)/(length - 1)*float(sv[0])
					#v = float(diagonal)/(length - 1)*float(sv[1])
				else:
					v = float((length-1)*2 - diagonal)/(length -1)*float(sv[0])
					#v = float((length-1)*2 - diagonal)/(length -1)*float(sv[1])
				mycolor = pygame.Color(0,0,0,255)
				mycolor.hsva = (odcien*360/float(self.frameRate), s, v, 100.0)
				entry = arrayFrame[x][y]
				entry[0] = mycolor.r
				entry[1] = mycolor.b
				entry[2] = mycolor.g
		return arrayFrame
	def __getitem__(self, index):
		return self.frames[index]
	def __len__(self):
		return self.frameRate

class Wheel(object):
	def __init__(self, rainbow, position = 0):
		self.position = position
		self.rainbow = rainbow
	def next(self):
		self.position += 1
		if self.position == len(self.rainbow) - 1:
			self.position = 0
		return self.rainbow[self.position]

[].append
class Wall(object):
	def __init__(self, plik, segmentSize):
		self.surface = pygame.image.load(plik)
		self.rect = self.surface.get_rect()
		self.segmentSize = segmentSize
		if not(self.rect[2] == self.rect[3] == segmentSize):
			#raise Warning("couldn't load the proper wall, using brown square: bad size of the " + str(plik) + " file. Use 8x8 .bmp")
			properSize = (int(segmentSize),int(segmentSize))
			self.surface = pygame.Surface(properSize)
			self.surface.fill(pygame.Color("brown"))
		self.collisions = {}
		self.rects = []
	def point(self, topLeft):
		blitAt = (topLeft[0], topLeft[1], segmentSize, segmentSize,)
		self.rects.append(blitAt)
		self.collisions[tuple(blitAt[:2])] = True
	def lineVertical(self, startAt, squaresNumber):
		for xCoord in range(squaresNumber):
			self.point((startAt[0], startAt[1] + xCoord*segmentSize,))	
	def lineHorizontal(self, startAt, squaresNumber):
		for yCoord in range(squaresNumber):
			self.point((startAt[0] + yCoord*segmentSize, startAt[1],))
	def collide(topleft):
		if topLeft in selfcollisions:
			return True
		else:
			return False
	def giveRecs(self):
		return self.rects
	def giveSurface(self):
		return self.surface
		
class Game(object): # have not been tested yet, relying on main loop in form of a script below
	def start(self, pygameApi, segmentSize, screenSize):
		self.pygameApi = pygameApi
		self.pygameApi.init()
		self.segmentSize = segmentSize
		self.screen = screenSize
		self.snakes = []
		self.walls = []
		self.globalVars()
	def globalVars(self):
		self.down = [0,1]
		self.up = [0,-1]
		self.right = [1,0]
		self.left = [-1,0]
		self.directions = [self.down, self.up, self.right, self.left]
	def snakeColoursWithRainbow(rainbowClass = Rainbow, frameRate = 91):
		self.rainbow = rainbowClass()
	def snakeColoursWithFile():
		pass
	def addSnake(self, length, positionAtStart, downUpRightLeftKeyset, directionAtStart, snakeClass = Snake, colourShift = 0, wheelClass = Wheel):
		keyset = {}
		for index, key in enumerate(downUpRightLeftKeySet):
			keyset[self.pygameApi.key] = self.directions[index]
		snake = snakeClass(length, Wheel(myRainbow), self.segmentSize, keyset = keySet, position = positionAtStart, direction = directionAtStart)
		self.snakes.append(snake)
	def addWalls(wallClass):
		pass	

pygame.init()
segmentSize = 8
size = width, height = segmentSize*100, segmentSize*76

#size = width, height = 1246, 1124

screen = pygame.display.set_mode(size)

down = [0,1]
up = [0,-1]
right = [1,0]
left = [-1,0]

myRainbow = Rainbow(91, (89.0, 51.0,), segmentSize)
marlosRainbow = Rainbow(6, (89.0, 51.0,), segmentSize)

wall = Wall("wall.bmp", segmentSize)
snake1 = Snake(40, Wheel(myRainbow), segmentSize, keyset = {pygame.K_UP : up, pygame.K_DOWN : down, pygame.K_RIGHT : right, pygame.K_LEFT : left}, position = [width - 2*segmentSize ,height/2], direction = left)
snake2 = Snake(8, Wheel(marlosRainbow), segmentSize, keyset = {pygame.K_w : up, pygame.K_s : down, pygame.K_d : right, pygame.K_a : left}, position = [0,height/2], direction = right)
#snake3 = Snake(60, Wheel(myRainbow, position = 480*2), segmentSize, keyset = {pygame.K_KP8 : up, pygame.K_KP5 : down, pygame.K_KP6 : right, pygame.K_KP4 : left}, position = [width/2,0], direction = down)
snakes = [snake1]#, snake2]#, snake2]#, snake3]
screen.fill(screenColour)
wall.lineHorizontal((0,0),100)
wall.lineVertical((0,0),76)
wall.lineHorizontal((0,height/2),25)
wall.lineVertical((0,height/2),25)
wall.lineVertical((64, height/2),25)
wall.lineHorizontal((0,height - segmentSize),100)
wall.lineVertical((width - segmentSize,0),76)
for entry in wall.giveRecs():
	screen.blit(wall.giveSurface(), entry)
pygame.display.update()
#print wall.collisions.keys()
while True:
	dirty = []
	"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			for snake in snakes:
				snake.keyStroke(event.key)
	"""
	queue = pygame.event.get()
 	if len(queue) != 0:
 		firstEvent = queue[-1]
	if firstEvent.type == pygame.QUIT:
		sys.exit()
	if firstEvent.type == pygame.KEYDOWN:
		for snake in snakes:
			snake.keyStroke(firstEvent.key)

	for snake in snakes:
		snake.move(dirty, wall.collisions)
	for entry in dirty:
		screen.blit(entry[0],entry[1])
	pygame.display.update([entry[1] for entry in dirty])
	pygame.time.wait(40)
