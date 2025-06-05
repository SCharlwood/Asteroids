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
	font = pygame.font.SysFont(None, 24)
	
	# Set groups
	updatable = pygame.sprite.Group()
	drawable  = pygame.sprite.Group()
	asteroids   = pygame.sprite.Group()
	shots         = pygame.sprite.Group()
	explosions  = pygame.sprite.Group()
	packs         = pygame.sprite.Group()
	
	
	#Setout Containers on Class objects
	Player.containers          = (updatable,drawable)
	Asteroid.containers       = (asteroids, updatable,drawable)
	AsteroidField.containers = (updatable)
	Explosion.containers      = (updatable,drawable)
	Shot.containers            = (shots, updatable,drawable)
	Pack.containers   = (packs, updatable,drawable) 
	
	
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
		
		# Asteroid Collisions detect
		for a in asteroids:
			# Does it collide with the Player?
			if P1.Does_Collide(a):
				P1.Health -=1
				a.kill()
				if P1.Health <=0:
					sys.exit("Game Over!")
				
			# Does asteroid collide with a shot?
			for s in shots:
				if a.Does_Collide(s):
					a.split(screen)
					s.kill()
					P1.Score +=1
		
		# Pack Collision detect
		for p in packs:
			if P1.Does_Collide(p):
				#determine what type of pack
				p.Add_To_Player(P1)

				p.kill()	

		
		for d in drawable:
			d.draw(screen)
		
		P1.WriteScore(screen,font)
		
		
		dt = clock.tick(60)/1000
		pygame.display.flip()












if __name__ == "__main__":
    main()
