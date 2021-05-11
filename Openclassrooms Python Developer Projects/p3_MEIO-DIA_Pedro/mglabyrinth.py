#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Labyrinth Game
Game in which MacGyver with his home made lethal weapon has to find and
kill the gard.

Python scripts
files: mglabyrinth.py, Level.py, constants.py, n1 + images
"""

# Import modules and packages
import pygame as pygame

from mg_labyrinth_classes.Level import *
from mg_labyrinth_classes.Personage import *
from constants import *
import time


def main():

	# Pygame in itialization
	pygame.init()

	# Enable to display text
	pygame.font.init()

	# Opening the Pygame window
	window = pygame.display.set_mode((SIDE_WINDOW, SIDE_WINDOW))
	# Icon
	icon = pygame.image.load(ICON_IMAGE)
	pygame.display.set_icon(icon)
	# Title
	pygame.display.set_caption(WINDOW_TITLE)

	# Principal loop
	continue_ = 1
	while continue_:
		# Loading and displaying the home screen
		home = pygame.image.load(HOME_IMAGE).convert()
		window.blit(home, (0, 0))

		# Refreshing the screen
		pygame.display.flip()

		# We reset these variables to 1 at each loop
		continue_game = 1
		continue_home = 1

		# While loop for the home window
		while continue_home:

			# Loop speed limitation
			pygame.time.Clock().tick(30)

			for event in pygame.event.get():

				'''If the user exits, we put the variables
				of the loop to 0 as to stop the loop and quit'''
				if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
					continue_home = 0
					continue_game = 0
					continue_ = 0
					# Variable for the level number
					choice = 0

				elif event.type == KEYDOWN:
					# Launch level 1
					if event.key == K_RETURN:
						continue_home = 0  # quit home
						choice = 'n1'  # define the level

		'''We check that the player has made a choice of level
		to not load if he leaves'''
		if choice != 0:
			# Bring up the background image
			background_img = pygame.image.load(BACKGROUND_IMAGE).convert()

			# Generate the level from a file
			level = Level(choice)
			level.generate()
			level.show(window)

			# Creation of MacGyver's person
			mg = Personage("images/mg_right.png", "images/mg_left.png",
						"images/mg_up.png", "images/mg_down.png", level)

		# GAME LOOP
		while continue_game:

			# Loop speed limitation
			pygame.time.Clock().tick(30)

			for event in pygame.event.get():

				'''If the user exits, we put the variable that continues the game
				AND ET the general variable to 0 to close the main window'''
				if event.type == QUIT:
					continue_game = 0
					continue_ = 0

				elif event.type == KEYDOWN:
					# SIf the user presses Esc here, we only return to the main_window
					if event.key == K_ESCAPE:
						continue_game = 0

					# Keys to move MacGyver around
					elif event.key == K_RIGHT:
						mg.move('right')
					elif event.key == K_LEFT:
						mg.move('left')
					elif event.key == K_UP:
						mg.move('up')
					elif event.key == K_DOWN:
						mg.move('down')

			# Show new positions
			window.blit(background_img, (0, 0))
			level.show(window)
			window.blit(mg.direction, (mg.x, mg.y))  # mg.direction = image with good direction
			pygame.display.flip()

			# Ready to strike is now 0, when it's 3 MacGyver can strike the ennemy
			ready_to_strike = 0
			# Three loops to see if all the objects have been picked up
			for x in range(0, 3):
				# Check if the positions of the objects are in the list of
				# all the paths MacGyver has been
				if level.three_xy_of_objetcs[x] in level.mgpaths:
					# Add 1 to ready to strike
					ready_to_strike += 1

			# Set the font text and its size to appear on the screen
			font = pygame.font.SysFont('Comic Sans MS', 13)
			# The texts to appear on the screen and their positions
			text1 = font.render("Objects picked up:", True, [255, 255, 255])

			text2 = font.render("{} of 3".format(
				ready_to_strike), True, [255, 255, 255])

			window.blit(text1, (330, 360))
			window.blit(text2, (360, 390))
			pygame.display.flip()

			# Victory -> Return to home screen
			if level.structure[mg.step_y][mg.step_x] == 'a':
				print(ready_to_strike)

				if ready_to_strike == 3:
					print('You won!')
					won = pygame.image.load(YOU_WON_IMAGE).convert_alpha()
					window.blit(won, (150, 150))
					pygame.display.flip()
					time.sleep(3)
					continue_game = 0

				else:
					print('You lost')
					lost = pygame.image.load(YOU_LOST_IMAGE).convert_alpha()
					window.blit(lost, (150, 150))
					pygame.display.flip()


if __name__ == "__main__":
	main()
