import pygame, random, math, numpy
g_screenSize = g_width, g_height = 600, 600

class Circle:
	def __init__(self, surfaceToBlit, radius = 10, color = pygame.Color("green"), position = None, angle = None, speed = 1):
		self.surfaceToBlit = surfaceToBlit
		self.radius = radius
		self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		self.position = self.initializePosition(position) 
		self.angle = self.initializeAngle(angle) * speed
		self.currentRectangle = self.plotPure()
		self.oldRectangle = self.currentRectangle
		self.speedUpdate = None
		self.checkedForCollisions = True
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
		return [self.currentRectangle.union(self.oldRectangle)]#, self.oldRectangle]
	def wallCollision(self):
		futurePosition = self.position + self.angle
		if futurePosition[0] >= g_width - self.radius or futurePosition[0] <= self.radius:
			self.angle[0] = (-1) * self.angle[0]
		if futurePosition[1] >= g_height - self.radius or futurePosition[1] <= self.radius:
			self.angle[1] = (-1) * self.angle[1]
	def updateSpeed(self, newSpeed):
		self.speedUpdate = newSpeed
	def move(self):
		if self.speedUpdate != None:
			self.angle = self.speedUpdate
			self.speedUpdate = None
		self.wallCollision()
		self.position = self.position + self.angle
		self.plot()

class Dots:
	#static methods
	@staticmethod
	def distanceBetweenMiddles(circleA, circleB):
		futureAPosition = circleA.position + circleA.angle
		futureBPosition = circleB.position + circleB.angle
		return futureAPosition - futureBPosition
	@staticmethod
	def detectCollision(circleA, circleB):
		distance = Dots.distanceBetweenMiddles(circleA, circleB)
		radiiSum = circleA.radius + circleB.radius
		return numpy.linalg.norm(distance) <= radiiSum
	@staticmethod
	def momentumExchange(circleA, circleB):
		#Both variables are numpy vectors
		normalVector = Dots.distanceBetweenMiddles(circleA, circleB)
		commonFactor = normalVector/numpy.dot(normalVector, normalVector)
		normalComponentA = numpy.dot(circleA.angle, normalVector)*commonFactor
		normalComponentB = numpy.dot(circleB.angle, normalVector)*commonFactor
		#leaving an update for the next step:
		circleA.updateSpeed(circleA.angle - normalComponentA + normalComponentB)
		circleB.updateSpeed(circleB.angle - normalComponentB + normalComponentA)
	#constructor
	def __init__(self, listOfObjects):
		self.dict = dict.fromkeys(listOfObjects)
		
	def resolveCollisions(self):
		for circleA in self.dict.keys():
			circleA.checkedForCollisions = False
		for circleA in self.dict.keys():
			circleA.checkedForCollisions = True
			for circleB in self.dict.keys():
				if circleB.checkedForCollisions != True:
					if circleA is not circleB and Dots.detectCollision(circleA, circleB):
						Dots.momentumExchange(circleA, circleB)

	def move(self):
		self.resolveCollisions()
		for circle in self.dict.keys():
			circle.move()

	def reportRecs(self):
		listOfRecs = []
		for circle in self.dict.keys():
			listOfRecs += circle.reportRecs()
		return listOfRecs
		
class Game:
	def __init__(self, screenSize):
		pygame.init()
		self.screen = pygame.display.set_mode(screenSize)
		self.secondScreen = pygame.display.set_mode(screenSize)
	def handleEvents(self):
		queue = pygame.event.get()
		for event in queue:
			if event.type == pygame.QUIT:
				quit()
	def gameLoop(self):
		listOfCircles = [Circle(self.screen, speed = 1) for i in range(15)]
		#circleA = Circle(self.screen, position = [g_width - 10, g_height - 11], angle = [0.0, 0.0])
		#circleB = Circle(self.screen, position = [g_width/2, g_height/2], angle = [1.0, 1.0])
#		listOfCircles = [circleA, circleB]
		dots = Dots(listOfCircles)
		while True:
		#	print circleA.position, circleB.position
			self.handleEvents()			
			self.screen.fill((0,0,0))
		#	print circleA.position, circleA.angle, circleB.position, circleB.angle
			dots.move()
			#print dots.reportRecs()
			pygame.display.update(dots.reportRecs())
			#pygame.time.wait()

game = Game(g_screenSize)
game.gameLoop()


