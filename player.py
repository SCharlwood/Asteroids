import pygame
from constants import *
from shot import Shot
from circleshape import CircleShape


class Player(CircleShape):
	
	def __init__(self , x, y,PLAYER_RADIUS):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.ShotTimer = 0
		self.Health =3
	
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
	
	
	def draw(self, screen):
		if self.Health ==3:
			SpriteColour = "green"
		elif self.Health ==2:
			SpriteColour = "orange"
		elif self.Health ==1:
			SpriteColour = "red"
			
		pygame.draw.polygon(screen, SpriteColour, self.triangle(), 2)
	
	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED*dt
	
	def update(self, dt):
		keys = pygame.key.get_pressed()
		
		# Rotate
		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		# Move forward or back
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
			
		# Shoot
		if self.ShotTimer >0:
			self.ShotTimer -= dt
			
		if keys[pygame.K_SPACE]:
			self.shoot()
			
	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt
		
	def shoot(self):
		if self.ShotTimer <= 0:
			s = Shot(self.position[0], self.position[1], SHOT_RADIUS)
			s.velocity =  pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
			self.ShotTimer = PLAYER_SHOOT_COOLDOWN
