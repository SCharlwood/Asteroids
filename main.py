import pygame
from constants import *
from circleshape import *
from player import *

# Internal Timing


def main():
	pygame.init()
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0 
	
	updatable = pygame.sprite.Group()
	drawable  = pygame.sprite.Group()
	Player.containers = (updatable,drawable)
	
	# Initialise Player character
	P1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
	
	# Game loop 
	check = 0
	while check == 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		
		# Update and Draw all objects
		updatable.update(dt)
		
		for d in drawable:
			d.draw(screen)
		
		dt = clock.tick(60)/1000
		pygame.display.flip()












if __name__ == "__main__":
    main()
