#!/usr/bin/python
import pygame, sys, numpy as np, math

class HeavyObject(object):
	def __init__(self, initialPosition, initialSpeed, mass):
		self.mass = mass
		self.position = np.array(initialPosition, dtype=float)
		self.speed = np.array(initialSpeed, dtype=float)
	def getMass(self):
		return self.mass
	def getPosition(self):
		return self.position
	def getSpeed(self):
		return self.speed
	def updateState(self, netAccelerationVector, fractionOfTime):
		speedChange = netAccelerationVector * fractionOfTime
		self.updateSpeed(speedChange)
		positionChange = self.getSpeed() * fractionOfTime
		self.updatePosition(positionChange)
	def updatePosition(self, byVector):
		self.position += byVector
	def updateSpeed(self, byVector):
		self.speed += byVector		

class SimplePlanet(HeavyObject):
	def __init__(self, initialPosition, initialSpeed, mass, radius = 16, colour="skyblue"):
		HeavyObject.__init__(self, initialPosition, initialSpeed, mass)
		self.colour = colour
		self.radius = radius
	def getCoordinates(self):
		return [int(i) for i in self.position]
	def plot(self, surface):
		return pygame.draw.circle(surface, pygame.Color(self.colour), self.getCoordinates(), self.radius)
		
class System():
	def __init__(self, listOfHeavyObjects, fractionOfSecond = 0.1, gConstant = 100.0):
		self.listOfHeavyObjects = listOfHeavyObjects
		self.massCentrePosition = np.array((0.0,0.0), dtype=float)
		#self.massCentreMass = 0
		self.fractionOfSecond = fractionOfSecond
		self.gConstant = gConstant
	"""
	def computeMassCentre(self, without):
		for heavyObject in self.listOfHeavyObjects:
			mass = heavyObject.getMass()
			position = heavyObject.getPosition()
			print position
			self.massCentreMass += mass
			self.massCentrePosition += position * mass
		self.massCentrePosition = self.massCentrePosition/self.massCentreMass
	
	def getMassCentre(self):
		return (self.massCentrePosition, self.massCentreMass)
	def computeAccTowardsMassCentre(self, Planet):
		massCentre = self.getMassCentre()
		print massCentre
		massCentrePosition = massCentre[0]
		massCentreMass = massCentre[1]
		deltaPosition = massCentrePosition - Planet.getPosition()
		planetMass = Planet.getMass()
		accelerationScalar = (self.gConstant * massCentreMass) / deltaPosition.dot(deltaPosition)
		print deltaPosition.dot(deltaPosition)
		return accelerationScalar
	"""
	def computeAccOfTwo(self, planetFor, planetTo):
		deltaPosition = planetTo.getPosition() - planetFor.getPosition()
		lengthSquare = deltaPosition.dot(deltaPosition)
		normalVector = deltaPosition/math.sqrt(lengthSquare)
		accelerationVector = ((self.gConstant * planetTo.getMass()) / lengthSquare) * normalVector
		return accelerationVector
	def computeAccVsOthers(self, planetFor):
		accelerationVector = np.array((0,0,))
		for planet in self.listOfHeavyObjects:
			accelerationVector += self.computeAccOfTwo(planetFor, planet)
		return accelerationVector
		
	def play(self, size):
		pygame.init()
		screen = pygame.display.set_mode(size)
		#miliseconds = int(self.fractionOfSecond * 1000)
		#screen.fill(pygame.Color("black"))	
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			for planet in self.listOfHeavyObjects:
				acc = self.computeAccVsOthers(planet)
				planet.updateState(acc, self.fractionOfSecond)
				planet.plot(screen, radius=10)
			screen.fill(pygame.Color("black"))
			screen.update()
				
			"""sun = self.listOfHeavyObjects[0]
			earth = self.listOfHeavyObjects[1]
			sunAcc = self.computeAccOfTwo(sun, earth)
			earthAcc = self.computeAccOfTwo(earth, sun)
			sun.updateState(sunAcc, self.fractionOfSecond)
			earth.updateState(earthAcc, self.fractionOfSecond)
			screen.fill(pygame.Color("black"))
			sunRect = sun.plot(screen)
			earthRect = earth.plot(screen)
			dirtyRect = (sunRect, earthRect)
			"""
			pygame.display.update()
			
		

size = width, height = (800, 600)
Sun = SimplePlanet([400, 300], [2, 1], 10)
Earth = SimplePlanet([300, 400], [-2, -1], 30)
system = System([Earth, Sun])
system.play(size)
#system.computeMassCentre()
#print system.computeAccOfTwo(Sun, Earth)
