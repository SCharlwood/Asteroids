import pygame
from constants import *
from circleshape import CircleShape
import random
import math

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		
	def draw(self, screen):
		pygame.draw.circle(screen, "white",self.position, self.radius, width = 2)
		
	def update(self, dt):
		self.position += self.velocity * dt
	
	def split(self,screen):
		
		self.kill()
		e   = Explosion(self.position[0], self.position[1], self.radius)
		if random.randint(1,HP_SPAWN_PROB) == 1:
			hp = Pack(self.position[0], self.position[1], HEALTH_PACK_SIZE)
		
		if self.radius <= ASTEROID_MIN_RADIUS:
			pass
		else:
				ang = random.uniform(20,50)
				s = Asteroid(self.position[0], self.position[1], self.radius-ASTEROID_MIN_RADIUS)
				s.velocity =  self.velocity.rotate(ang) *1.2
				
				ss = Asteroid(self.position[0], self.position[1], self.radius-ASTEROID_MIN_RADIUS)
				ss.velocity =  self.velocity.rotate(-ang)  *1.2
	
	
	
				 


class Explosion(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		self.N_Points = random.randint(5,10)
		self.Ang = 360/self.N_Points
		self.time = Explode_Time
		self.DrawRadius = 0
		
		
	def draw(self, screen):
		pygame.draw.polygon(screen, "yellow", self.ExplodePoly(self.DrawRadius), 2)
		
	def update(self, dt):
		# Update Draw radius

		self.DrawRadius = (1-math.cos(self.time*2*3.1412/Explode_Time)) * 0.5 *  self.radius
		
		if self.time <= 0:
			self.kill()
		else:
			self.time -= 1
		
		
	def ExplodePoly(self,radius):
		Star_Points = []
		
		for i in range(self.N_Points):
			Star_Points.append(self.position + pygame.Vector2(0, 1).rotate(i*self.Ang)*radius*1.25)
			Star_Points.append(self.position + pygame.Vector2(0, 1).rotate(i*self.Ang+0.5*self.Ang)*radius*0.75)

		return Star_Points


class Pack(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		self.HPValue = 1
		
		if random.getrandbits(1) ==1:
			self.type = "health"
			self.Value = 1
			self.colour = "green"
		else:
			self.type = "ammo"
			self.Value = 20
			self.colour = "blue"
		
	def Add_To_Player(self,Player):
		
		if 	 self.type == "health":
			if Player.Health<PLAYER_MAX_HEALTH:
				Player.Health +=self.Value
				if Player.Health>PLAYER_MAX_HEALTH:
					Player.Health=PLAYER_MAX_HEALTH
		
		elif 	 self.type == "ammo":
			if Player.ammo<MAX_AMMO:
				Player.ammo +=self.Value
				if Player.ammo>MAX_AMMO:
					Player.ammo=MAX_AMMO

		
		
	def draw(self, screen):
		pygame.draw.circle(screen, self.colour,self.position, self.radius, width = 2)
		
	def update(self, dt):
		# Update Draw radius
		# Maybe add a fading functionality ?????
		pass

	
