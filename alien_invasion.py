import sys

import pygame

from settings import Settings

def run_game():
	#initialize game and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#set the background colour.
	bg_colour = (230, 230 , 230)

	#Start the main loop for the game.
	while True:

		#watch for keyboard and mouse events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		#Redraw the screen during each pass through loop
		screen.fill(ai_settings.bg_colour)

		#make the most recently drawn screen visible.
		pygame.display.flip()


run_game()