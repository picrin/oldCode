# Copyright (C) 2012, Adam Kurkiewicz and Thomas Wallis.
# Send any queries to adam@kurkiewicz.pl, tom@tom-wallis.com
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame, random, math, numpy, bintrees, copy, pdb
g_screenSize = g_width, g_height = 600, 600

class Wall:
	def __init__(self, horizontal):
		if horizontal is True:
			self.orientation = 0
		else: #horizontal is False:
			self.orientation = 1

class Collision(absoluteTime):
	def __init__(self, absoluteTime)
		self.absoluteTime = absoluteTime
	def __cmp__(self, otherCollision):
		if self.absoluteTime < otherCollision.absoluteTime:
			return -1
		elif self.absoluteTime > otherCollision.absoluteTime:
			return 1
		else:
			return 0
	#Dammit, where are the fucking interfaces python?!
	def resolveCollision():
		pass
	def report(circleHash, circleBinTree):
		pass

class WallCollision(Collision):
	def __init__(self, absoluteTime, circle):
		Collision.__init__(absoluteTime)
		self.circle = circleA

	def report(circleHash, circleBinTree):
		pass

class CircleCollision
		self.circleA = circleA
		self.circleB = circleB
		self.wallCollision = False
		

class Circle:
	def __init__(self, surfaceToBlit, radius = 10, color = None, position = None, angle = None, speed = 1):
		"""
		@end-user -- creates a circle that can move and bounce from walls and other circles. Momentum is exchanged with regards to the energy and momentum conservation laws within @surfaceToBlit. Underlying collision algorithm is triggered off only in frames with occurying collisions and works in O(n) time, where n is the number of objects. Collison free frames are computed at low cost in simply 2n basic vector operations. Position vectors are updated only during collisions, hence model is quite stable numerically (as little iterations as possible).
		@surfaceToBlit -- the screen or (less likely) the other surface to blit to.
		@radius -- radius of the circle
		@color -- color of the circle in RGB tuple e.g. (0, 255, 0). If None, initialized randomly.
		@position -- position of the circle from top left @surfaceToBlit corner in iterable of length 2 in pixels, e.g. [200, 2]. 
		@angle -- angle of initial motion as a numeral from [0, 2*pi] or None to initialize randomly. E.g. 0 for horizontal movement.
		@speed -- desired length of velocity vector in pixels per time frame. Defaults to 1.
		"""
		# general attributes, frequently used for both algorithm and plotting.
		self.radius = radius
		self.position = self.initializePosition(position)
		self.velocity = self.initializeVelocity(angle) * speed
		
		# attributes specifically for underlying collision algorithm.
		self.timeSinceCollision = float(0)
		self.timeNextCollision = None # this one is a filthy (impure :D ) mutable disaster, I think I should remove it and resolve all handles.
		#self.lastObjectCollidedWith = None
		
		#TODO -- attributes for evolution... if any ?! Maybe splitting done through dots...
		
		# attributes that are primarily used for visual representation
		self.surfaceToBlit = surfaceToBlit
		self.color = self.initializeColor(color) 
		self.currentRectangle = self.plotPure() # already appears on the screen.
		self.oldRectangle = self.currentRectangle
	def initializePosition(self, position):
		"""
		@dev-only
		initializes the position vector with uniform probability throughout the available screen space, or passes user's position. Constructor extension.
		@position -- user's position or None for random initialization
		@return -- position vector
		"""
		#TODO initialization should be first checking for any potential collisions with objects already initialized!
		#Why not to do it in the Dots class?
		if position is None:
			return numpy.array([random.uniform(0 + self.radius, g_width - self.radius), random.uniform(0 + self.radius, g_height - self.radius)], dtype=float)
		else:
			return numpy.array(position, dtype=float)
	def initializeVelocity(self, angle):
		"""
		@dev-only
		initializes a random unit vector with uniform circular distribution, or passes user's angle
		@angle -- user's angle or None for random initialization.
		@return -- velocity vector
		"""
 		if angle is None:
			unitVelocity = random.uniform(0, 2*math.pi)
			return numpy.array([math.cos(unitVelocity), math.sin(unitVelocity)], dtype=float)
		else:
			return numpy.array([math.cos(angle), math.sin(angle)], dtype=float)
	def initializeColor(self, color):
		"""
		@dev-only
		initializes a random color as a tuple (r, g, b), or passes user's color, like pygame.Color("green")
		@color -- user's color or None for random initialization.
		"""
		if color is None:
			return [random.randint(0,255) for i in range(3)]
		else:
			return color
	def plotPure(self):
		"""
		@dev-only -- plotting a circle (as a side effect) on the @surfaceToBlit returning a rectangle that conatins the circle. Without updating the self.currentRectangle and self.oldRectangle attributes.
		"""
		return pygame.draw.circle(self.surfaceToBlit, self.color, [int(number) for number in (self.position + self.timeSinceCollision*self.velocity)], self.radius)
	def plot(self):
		"""
		@end-user -- this is the function used for plotting the circle (as a side effect). If using dirty recs screen update use the rectangle returned by reportRecs()
		"""
		self.oldRectangle = self.currentRectangle
		self.currentRectangle = self.plotPure()
	def reportRecs(self):
		"""
		@end-user
		@return -- returns the rectangle which includes both areas that have been changed since last move. Increases performance drastically when passed to pygame.display.update function.
		"""
		return [self.currentRectangle.union(self.oldRectangle)] # this is a nice trick to update only those parts of the screen that need updating.
#	def updateLastCollided(self, wallOrCircle):
#		self.lastObjectCollidedWith = wallOrCircle
	def expectedWallCollision(self, threshold = 10**-2):
		"""
		@dev-only -- working out the earliest wall collision. Should be fed as the first value for expected time collision, whenever updating the collisions for 
		"""
		solutions = []
		wallsHorizontal = [self.radius, g_width - self.radius]
		wallsVertical = [self.radius, g_height - self.radius]
		for horizontal in wallsHorizontal:
			solution = Numerical.solveLinear([self.velocity[0], self.position[0] - horizontal])
			if solution is not None and solution > threshold:
				solutions.append((solution, Wall(True),))
		for vertical in wallsVertical:
			solution = Numerical.solveLinear([self.velocity[1], self.position[1] - vertical])
			if solution is not None and solution > threshold:
				solutions.append((solution, Wall(False),))
		if len(solutions) == 0:
			raise Exception("should be min of at least two.")
		return min(solutions)
	def expectedCircleCollision(self, circle):
		positionDifference = self.position - circle.position
		velocityDifference = self.velocity - circle.velocity
		radiiSum = self.radius + circle.radius
		leadingCoefficient = velocityDifference[0]**2 + velocityDifference[1]**2
		middleCoefficient = 2*(velocityDifference[0]*positionDifference[0] + velocityDifference[1]*positionDifference[1])
		constantCoefficient = positionDifference[0]**2 + positionDifference[1]**2 - radiiSum**2
		time = Numerical.solveQuadraticPrune([leadingCoefficient, middleCoefficient, constantCoefficient])
		return (time, circle,)
	def soonestCollision(self, listOfCircles):
		wallCollision = self.expectedWallCollision()
		circleCollision = []
		for circle in listOfCircles:
			expectedTime = self.expectedCircleCollision(circle)
			if expectedTime[0] is not None:
#				print expectedTime
				circleCollision.append(expectedTime)
	#	circleCollision = [self.expectedCircleCollision(circle) for circle in listOfCircles]
		if len(circleCollision) != 0:
#			print min(circleCollision)
			soonestCollision = min([min(circleCollision), wallCollision])
		else:
			soonestCollision = wallCollision
		return soonestCollision
#	def firstStepCollisionUpdate(self):
#		self.timeNextCollision = self.expectedWallCollision()[0]
#	def nextStepCollisionUpdate(self, circle):
#		updateTimeNextCollision = self.expectedCircleCollision(circle)
#		if updateTimeNextCollision is not None and updateTimeNextCollision < self.timeNextCollision:
#			self.timeNextCollision = updateTimeNextCollision
	def nextFrame(self):
		self.timeSinceCollision += 1
#	def nextFrameNoCollision(self):
#		if self.timeSinceCollision + 1 < self.timeNextCollision:
#			return True
#		else:
#			return False
	def updatePosition(self): # do it before handling collisions
		self.position = self.position + self.velocity * self.timeNextCollision
	def handleCollision(self, newVelocity):
		#timeLeftOver = self.timeSinceCollision - self.timeNextCollision
		#self.timeSinceCollision = timeLeftOver
		#self.timeSinceCollision = 0
		#F< -self.timeNextCollision = None
		self.velocity = newVelocity
	def reverseMomentum(self, component):
		velocity = copy.copy(self.velocity)
		velocity[component] = -velocity[component]
		return velocity

class Numerical:
	@staticmethod
	# I would rather use this one over the alternative in the bottom, unless for
	# performance reasons. I don't want to rely on external libraries unless
	# necessary.
	def solveQuadraticPrune(equation):
		delta = equation[1]**2 - 4*equation[0]*equation[2]
		if delta < 0:
			return None
		else:
			solution = [((-equation[1] + delta**(1.0/2.0))/(2*(equation[0]))), ((-equation[1] - delta**(1.0/2.0))/(2*(equation[0])))]
			if min(solution) > 0:
				return min(solution)
			elif max(solution) > 0:
				return max(solution)
			else:
				return None
	@staticmethod
	def solveQuadraticPrune_(equation):
		solution = numpy.roots(equation) # well, maybe
		solution = numpy.real_if_close(numpy.roots(equation))
		#print solution
		return Numerical.solutionPruning(solution)
	@staticmethod
	def solutionPruning(twoSolutions):
		"""
		@dev-only -- return least real positive from a sequence of two complex numbers (or exceptionally one). If there is no such number, returns one.
		"""
		try:
			if twoSolutions[0].imag == 0:
				if min(twoSolutions) > 0:
					return min(twoSolutions)
				elif max(twoSolutions) > 0:
					return max(twoSolutions)
				else:
					return None		
			else:
				return None
		except IndexError:
			print "unusual stuff going on with solution pruning. Leading coefficient == 0?"
			return twoSolutions[0].real
	@staticmethod
	def solveLinear(equation):
		try:
			solution = -1 * equation[1]/equation[0]
			if solution > 0:
				return solution
			else:
				return None
			#a + bt = 0
			#bt = -a
			#t = -a/b
		except ZeroDivisionError:
			print "yo kiddin ma bleach, zero speed component da velocity vector?!"
			return numpy.finfo(float).max
class Dots:
	@staticmethod
	def distanceBetweenMiddles(circleA, circleB):
		return circleA.position - circleB.position
		#futureAPosition = circleA.position + circleA.velocity
		#futureBPosition = circleB.position + circleB.velocity
		#return futureAPosition - futureBPosition
	@staticmethod
	def detectCollision(circleA, circleB):
		distance = Dots.distanceBetweenMiddles(circleA, circleB)
		radiiSum = circleA.radius + circleB.radius
		return numpy.linalg.norm(distance) <= radiiSum
	@staticmethod
	def momentumExchange(circleA, circleB):
		#Both variables are numpy vectors
		if hasattr(circleA, 'orientation'): #in other words: if circleA is a wall	
			#circleB.updatePosition()
			circleB.handleCollision(circleB.reverseMomentum(circleA.orientation))
			return
		if hasattr(circleB, 'orientation'): #in other words: if circleB is a wall
			#circleA.updatePosition()
			circleA.handleCollision(circleA.reverseMomentum(circleB.orientation))
			return
		#circleA.updatePosition()
		#circleB.updatePosition()
		normalVector = Dots.distanceBetweenMiddles(circleA, circleB)
		commonFactor = normalVector/numpy.dot(normalVector, normalVector)
		normalComponentA = numpy.dot(circleA.velocity, normalVector)*commonFactor
		normalComponentB = numpy.dot(circleB.velocity, normalVector)*commonFactor
		circleANewVelocity = circleA.velocity - normalComponentA + normalComponentB
		circleBNewVelocity = circleB.velocity - normalComponentB + normalComponentA
		circleA.handleCollision(circleANewVelocity)
		circleB.handleCollision(circleBNewVelocity)
	def __init__(self, listOfCircles):
		self.punkt = False
		self.setOfCircles = set(listOfCircles)
		self.listOfCollisions = []
		for circle in listOfCircles:
			if len(self.setOfCircles) != 0:
				self.listOfCollisions.append(self.soonestCollision(circle, self.setOfCircles))
			self.setOfCircles.add(circle)
		self.listOfCollisions.sort()
		#for circle in listOfCircles:
		#	if len(self.setOfCircles) != 0:
		#		self.soonestCollision(circle, self.setOfCircles)
		#	self.setOfCircles.add(circle)
		#self.currentMin = self.BSTOfCircles.min_item()
	def moveCircles(self, time):
		#print time, self.currentMin
		if time < self.listOfCollisions[0]:
			for circle in list(self.setOfCircles):
				circle.nextFrame()
				circle.plot()
		else:
			self.ti(handleCollisionme)
	def soonestCollision(self, circle, setOfCircles, time = 0):
		"""
		@mutates -- mutates circle.timeNextCollision
		"""
		shortestTime = circle.soonestCollision(list(setOfCircles))
		compliantTime = shortestTime[0] + time
		#circle.timeNextCollision = shortestTime[0]
		#if not hasattr(shortestTime[1], "orientation"):
		#	shortestTime[1].timeNextCollision = shortestTime[0]
		return (compliantTime, (shortestTime[1], circle,))
		#self.BSTOfCircles.insert(compliantTime, (shortestTime[1], circle,))
		
	def handleCollision(self, time):
		#if self.punkt == False:
		#self.punkt = True
		#justTime = self.listOfCollisions[0][0]
		#circleAlikeA = self.listOfCollisions[0][1][0]
		#circleAlikeB = self.listOfCollisions[0][1][1]
		Dots.momentumExchange(circleAlikaA, circleAlikeB)
		
		#justTime = self.currentMin[0]
		#circleAlikeA = self.currentMin[1][0]
		#circleAlikeB = self.currentMin[1][1]
		#Dots.momentumExchange(circleAlikeA, circleAlikeB)
		#otherCircles = self.setOfCircles.difference(set([circleAlikeA, circleAlikeB]))
		#self.BSTOfCircles.pop(justTime)
		#self.soonestCollision(circleAlikeA, otherCircles, time)
		#self.soonestCollision(circleAlikeB, otherCircles, time)
		#self.currentmin = self.BSTOfCircles.min_item()
		#print self.currentmin, "\n\n\n\n\n\n\n\n\n"
		#else:
		#	pass
		
			
#	def resolveCollisions(self, listOfCircles = None):
#		for circle in listOfCircles:
#			soonestCollision = circle.soonestCollision(self.setOfCircles.keys())
#			self.BSTOfCircles.insert(circle, soonestCollision)
#			self.setOfCircles.add(circle)
	def initializeCircles(self):
		if listOfCircles is None:
			pass
		else:
			set.fromkeys(listOfCircles)
	def detectCollisions(self, circleA):
		return True or False

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
#		dots = Dots(listOfCircles)
#		#dots
#		collision = None
#		time = 0
#		while collision is None:
#			print "tusia"
#			self.handleEvents()
#			time += 1
#			self.screen.fill((0,0,0,))
#			for circle in listOfCircles:
#				circle.nextFrame()
#				print circle.velocity
#				print circle.timeSinceCollision
#				circle.plot()
#			collision = dots.moveCircles(time)
#			pygame.display.update()
#			pygame.time.wait(20)
			
		#wallInFrames = circleA.expectedWallCollision()
		#print wallInFrames, circleA.position + circleA.velocity


		"""
		dots = Dots([circleA, circleB])
		while time <= 61:
			time += 1
			self.handleEvents()
			self.screen.fill((0,0,0,))
			dots.moveCircles(time)
			pygame.display.update()
			pygame.time.wait(100)
	
		"""
		"""
		time = float(0)
		circleA = Circle(self.screen, position = [50, 100], angle = 0.0001, speed = 1)
		#circleB = Circle(self.screen, position = [150, 100], angle = math.pi + 0.0001, speed = 1)
		listOfCircles = [circleA]
		while True:
			tupleWithWall = circleA.soonestCollision([])
			circleA.timeNextCollision = tupleWithWall[0]
			compliantTime = tupleWithWall[0] + time
			print compliantTime
			while time < compliantTime:
				#print circleA.position, circleA.velocity
				#print circleB.position, circleB.velocity
				#print "-"*10
				time += 1
				self.handleEvents()	
				pygame.display.update()
				self.screen.fill((0,0,0))
				for circle in listOfCircles:
					circle.nextFrame()
					circle.plot()
					#print circle.timeSinceCollision
				pygame.time.wait(10)
			Dots.momentumExchange(tupleWithWall[1], circleA)
		"""
		
		#circleB = Circle(self.screen, position = [100, 100], angle = 99.01, speed = 1)
		#circleA = Circle(self.screen, position = [200, 200], angle = 100.01, speed = 1)
		
		#circleC = Circle(self.screen, position = [300, 300], angle = math.pi*5/4, speed = 0)
		#listOfCircles = [circleA, circleB]#, circleC]
		listOfCircles = [Circle(self.screen) for i in range(100)]
		time = float(0)
		while True:
			collisions = []
			for circle in listOfCircles:
				otherCircles = []
				for otherCircle in listOfCircles:
					if otherCircle is not circle:
						otherCircles.append(otherCircle)
				soonestCollisionOfCircle = circle.soonestCollision(otherCircles)
				SCoCwC = (soonestCollisionOfCircle[0], (soonestCollisionOfCircle[1], circle))
				collisions.append(SCoCwC)
			
			#soonestCollisionOfA = circleA.soonestCollision([circleB])#[circleB])#, circleC])
			#soonestCollisionOfB = circleB.soonestCollision([circleA])#, circleC])
			#soonestCollisionOfC = circleC.soonestCollision([circleA, circleB])
			#SCoAwithA = (soonestCollisionOfA[0], (soonestCollisionOfA[1], circleA,))
			#SCoBwithB = (soonestCollisionOfB[0], (soonestCollisionOfB[1], circleB,))
			#SCoAwithC = (soonestCollisionOfC[0], (soonestCollisionOfC[1], circleC,))
			
			soonestCollisionInASystem = min(collisions)#, SCoAwithC])
			#print soonestCollisionInASystem, time
			#print circleA.position
			#if not hasattr(soonestCollisionInASystem[1][0], 'orientation'):
				#soonestCollisionInASystem[1][0].timeNextCollision = soonestCollisionInASystem[0]
			#soonestCollisionInASystem[1][1].timeNextCollision = soonestCollisionInASystem[0]
			
			compliantTime = soonestCollisionInASystem[0] + time
			#pdb.set_trace()
			while time < compliantTime - 1:
				#print circleA.position, circleA.velocity
				#print circleB.position, circleB.velocity
				#print "-"*10
				#pdb.set_trace()
				
				self.handleEvents()	
				self.screen.fill((0,0,0))
				for circle in listOfCircles:
					circle.nextFrame()
					circle.plot()
					#print circle.timeSinceCollision
				
				pygame.display.update()
				pygame.time.wait(10)
				time += 1
			#pdb.set_trace()
			for circle in listOfCircles:
				circle.position = circle.position + circle.timeSinceCollision * circle.velocity
				circle.timeSinceCollision = 0
			Dots.momentumExchange(soonestCollisionInASystem[1][0], soonestCollisionInASystem[1][1])
			
			#pdb.set_trace()
		
#		while True:
#			time += 1
#			self.handleEvents()
#			pygame.display.update()
#			self.screen.fill((0,0,0))
#			for circle in listOfCircles:
#				circle.nextFrame()
#				circle.plot()
#				#print circle.timeSinceCollision
#			pygame.time.wait(10)
		
game = Game(g_screenSize)
game.gameLoop()
		
		

