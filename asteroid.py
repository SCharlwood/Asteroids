import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		
	def draw(self, screen):
		pygame.draw.circle(screen, "white",self.position, self.radius, width = 2)
		
	def update(self, dt):
		self.position += self.velocity * dt
	
	def split(self):
		
		self.kill()
		
		if self.radius <= ASTEROID_MIN_RADIUS:
			pass
		else:
				ang = random.uniform(20,50)
				s = Asteroid(self.position[0], self.position[1], self.radius-ASTEROID_MIN_RADIUS)
				s.velocity =  self.velocity.rotate(ang) *1.2
				
				ss = Asteroid(self.position[0], self.position[1], self.radius-ASTEROID_MIN_RADIUS)
				ss.velocity =  self.velocity.rotate(-ang)  *1.2
				 
