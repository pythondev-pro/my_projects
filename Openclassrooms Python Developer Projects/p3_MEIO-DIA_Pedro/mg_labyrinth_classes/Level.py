import pygame
from constants import *
import random


class Level:
    """class to create a new level"""

    def __init__(self, file='level_file.txt'):
        self.file = file
        self.structure = 0
        self.three_xy_of_objetcs = []
        self.paste_the_3_objects = []
        self.mgpaths = []

    def generate(self):
        """A method to generate the level according level's file.
        Create a general list, containing a list for each line"""
        # Open file
        with open(self.file, "r") as file:
            level_structure = []
            # for loop for the lines of the file
            for line in file:
                line_level = []
                # For loop for the sprites (letters) in each line
                for sprite in line:
                    # Ignoring the "\n" on the end of the line
                    if sprite != '\n':
                        # Appending the sprite to the list of the lines
                        line_level.append(sprite)
                # Appending the line to the list of the level_structure
                level_structure.append(line_level)
            # To save this structure
            self.structure = level_structure

    # Chosing three random numbers for the x position
    r_list = []
    while len(r_list) != 3:
        for d in range(0, 3):
            r = random.randint(0, 102)
            if r not in r_list:
                r_list.append(r)

    def show(self, window):
        xy_objetcs = []
        """Method for displaying the level according to the 
		structure's list from generate()"""
        # Loading images with transparency
        wall = pygame.image.load(WALL_IMAGE).convert()
        start = pygame.image.load(START_IMAGE).convert()
        arrived = pygame.image.load(ARRIVED_IMAGE).convert_alpha()
        syringe = [pygame.image.load(PLASTIC_PIPE_IMAGE).convert_alpha(),
                   pygame.image.load(ETHER_IMAGE).convert_alpha(),
                   pygame.image.load(NEEDLE_IMAGE).convert_alpha()]
        erase_object_image = pygame.image.load(MINI_BACKGROUND_IMAGE).convert()

        # For loop through the list of the leve
        num_line = 0
        for line in self.structure:
            # On parcourt les listes de lignes
            num_step = 0
            for sprite in line:
                # Calculate the x and y position in pixels
                x = num_step * SPRITE_SIZE
                y = num_line * SPRITE_SIZE
                if sprite == 'w':  # w = Wall
                    window.blit(wall, (x, y))
                elif sprite == 's':  # s = Start
                    window.blit(start, (x, y))
                elif sprite == 'a':  # a = Arrived
                    window.blit(arrived, (x, y))
                elif sprite == '0':  # 0 = free space
                    xy_objetcs.append([x, y])
                num_step += 1
            num_line += 1
        three_xy_of_objetcs = [xy_objetcs[self.r_list[n]] for n in range(
            0, 3)]  # selection les trois paires x et y au azar

        self.three_xy_of_objetcs = three_xy_of_objetcs
        # list to add the three objects randomly
        self.paste_the_3_objects.append([window.blit(syringe[i], (
            three_xy_of_objetcs[i][0],
            three_xy_of_objetcs[i][1])) for i in range(3)])

        for x in self.mgpaths:

            if x in self.three_xy_of_objetcs:
                window.blit(erase_object_image, (x[0], x[1]))
