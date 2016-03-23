#!/usr/bin/python
import pygame, sys, numpy, math

def length(a):
	return math.sqrt((a[0]**2 + a[1]**2))

def add(a,b):
	return [a[0] + b[0], a[1] + b[1]]

def subtract(a,b):
	return [a[0] - b[0], a[1] - b[1]]

def scalarMultiply(scalar, vector):
	return [scalar * vector[0], scalar * vector[1]]

def distance(a, b):
	return length(subtract(a,b))

def force(firstBodyPosition, firstBodyMass, secondBodyPosition, secondBodyMass, g = 4*10**4):
	return (g * firstBodyMass * secondBodyMass) / distance(firstBodyPosition, secondBodyPosition)**2
	
def normalize(vector):
	length = distance(vector,[0,0])
	return [vector[0]/length, vector[1]/length]

centrePosition = [350.0, 400.0]
initialSpeed = [70, -120]
initialPosition = [500.0, 500.0]

earthMass = 10.0
sunMass = 150.0

theta = 0.0
radius = 100.0
earthRadius = 10
sunRadius = 15

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)

seconds = 0.01


miliseconds = int(math.floor(seconds*1000))

currentSpeed = initialSpeed
currentPosition = initialPosition
sunSpeed = [0,0]
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	sunSpeed = add(sunSpeed, scalarMultiply(force(currentPosition, earthMass, centrePosition, sunMass)/sunMass*seconds, normalize(subtract(currentPosition, centrePosition))))
	currentSpeed = add(currentSpeed, scalarMultiply(force(currentPosition, earthMass, centrePosition, sunMass)/earthMass*seconds, normalize(subtract(centrePosition, currentPosition))))
	centrePosition = add(centrePosition, scalarMultiply(seconds, sunSpeed))
	currentPosition = add(currentPosition, scalarMultiply(seconds, currentSpeed))
	screen.fill(pygame.Color("black"))
	pygame.draw.circle(screen, pygame.Color("skyblue"), map(int,currentPosition), earthRadius)
	pygame.draw.circle(screen, pygame.Color("yellow"), map(int,centrePosition), sunRadius)
	pygame.display.update()
	pygame.time.wait(miliseconds)
