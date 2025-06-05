import sys
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

# Internal Timing


def main():
	pygame.init()
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0 
	
	# Set groups
	updatable = pygame.sprite.Group()
	drawable  = pygame.sprite.Group()
	asteroids  = pygame.sprite.Group()
	shots       = pygame.sprite.Group()
	
	#Setout Containers on Class objects
	Player.containers          = (updatable,drawable)
	Asteroid.containers       = (asteroids, updatable,drawable)
	AsteroidField.containers = (updatable)
	
	Shot.containers            = (shots, updatable,drawable)
	
	# Initialise Player character
	P1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
	AF = AsteroidField()
	
	# Game loop 
	check = 0
	while check == 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		
		# Update and Draw all objects
		updatable.update(dt)
		
		# Collision detect
		for a in asteroids:
			# Does it collide with the Player?
			if P1.Does_Collide(a):
				sys.exit("Game Over!")
				
			# Does asteroid collide with a shot?
			for s in shots:
				if a.Does_Collide(s):
					a.split()
					s.kill()
						
				
		
		for d in drawable:
			d.draw(screen)
		
		dt = clock.tick(60)/1000
		pygame.display.flip()












if __name__ == "__main__":
    main()
