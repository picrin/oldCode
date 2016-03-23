import pygame, random, math, numpy
g_screenSize = g_width, g_height = 800, 600

class Circle:
	def __init__(self, surfaceToBlit, radius = 10, color = pygame.Color("green"), position = None, angle = None):
		self.surfaceToBlit = surfaceToBlit
		self.radius = radius
		self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		self.position = self.initializePosition(position)
		self.angle = self.initializeAngle(angle)
		self.currentRectangle = self.plotPure()
		self.oldRectangle = self.currentRectangle
	def initializePosition(self, position):
		if position == None:
			return numpy.array([random.uniform(0 + self.radius, g_width - self.radius), random.uniform(0 + self.radius, g_height - self.radius)], dtype=float)
		else:
			return numpy.array(position, dtype=float)
	def initializeAngle(self, angle):
 		if angle == None:
			angleValue = random.uniform(0, 2*math.pi)
			return numpy.array([math.cos(angleValue), math.sin(angleValue)], dtype=float)
		else:
			return numpy.array(angle, dtype=float)
	def plotPure(self):
		return pygame.draw.circle(self.surfaceToBlit, self.color, [int(number) for number in self.position], self.radius)
	def plot(self):
		self.oldRectangle = self.currentRectangle
		self.currentRectangle = self.plotPure()
	def reportRecs(self):
		return [self.currentRectangle, self.oldRectangle]
	def distanceMiddleCircle(self, otherCircle):
		return self.position - otherCircle.position
	def detectCollision(self, otherCircle):
		distance = self.distanceMiddleCircle(otherCircle)
		radiiSum = self.radius + otherCircle.radius
		return numpy.linalg.norm(distance) <= radiiSum # return boolean
	def giveOffSpeed(self, otherCircle, speed):
		self.angle = self.angle - speed
		otherCircle.angle = otherCircle.angle + speed
				
	def collisionNormal(self, normalVector):
		shiftVector = numpy.dot(self.angle, normalVector)/numpy.dot(normalVector, normalVector)*normalVector
		#This would be very interesting physics indeed but COMPLETELY WRONG!!!
		#self.angle = self.angle - 2*shiftVector
		return shiftVector		
		#self.move()
	def collisionCircle(self, otherCircle):
		speedToGiveOff = self.collisionNormal(self.distanceMiddleCircle(otherCircle))
		self.giveOffSpeed(otherCircle, speedToGiveOff)
		#self.move()
	def wallCollision(self):
		if self.position[0] >= g_width - self.radius or self.position[0] <= self.radius:
			self.angle[0] = (-1) * self.angle[0]
		if self.position[1] >= g_height - self.radius or self.position[1] <= self.radius:
			self.angle[1] = (-1) * self.angle[1]
	def move(self, factor = 1):
		self.wallCollision()
		self.position = self.position + self.angle * factor
		self.plot()

class Dots:
	def __init__(self, listOfObjects):
		self.dict = dict.fromkeys(listOfObjects)
	def collide(self):
		for circleA in self.dict.keys():
			for circleB in self.dict.keys():
				if circleA != circleB:
					if circleA.detectCollision(circleB):
						circleA.collisionCircle(circleB)
	def move(self):
		for circleA in self.dict.keys():
			circleA.move()
			for circleB in self.dict.keys():
				if circleA != circleB:
					if circleA.detectCollision(circleB):
						circleA.collisionCircle(circleB)
						#circleA.move()
						#circleB.collisionCircle(circleA)
						#circleB.move()
	def reportRecs(self):
		listOfRecs = []
		for circle in self.dict.keys():
			listOfRecs += circle.reportRecs()
		return listOfRecs
		
class Game:
	def __init__(self, screenSize):
		pygame.init()
		self.screen = pygame.display.set_mode(screenSize)
	def handleEvents(self):
		queue = pygame.event.get()
		for event in queue:
			if event.type == pygame.QUIT:
				quit()
	def gameLoop(self):
#		listOfCircles = [Circle(self.screen) for i in range(10)]
		circleA = Circle(self.screen, position = [200, 200], angle = [10, 0])
		circleB = Circle(self.screen, position = [400, 200], angle = [-1, 0])
		listOfCircles = [circleA, circleB]
		dots = Dots(listOfCircles)
		while True:
		#	print circleA.position, circleB.position
			self.handleEvents()			
			self.screen.fill((0,0,0))
		#	print circleA.position, circleA.angle, circleB.position, circleB.angle
			dots.move()
			#print dots.reportRecs()
			pygame.display.update()#dots.reportRecs())
			pygame.time.wait(0)

game = Game(g_screenSize)
game.gameLoop()


