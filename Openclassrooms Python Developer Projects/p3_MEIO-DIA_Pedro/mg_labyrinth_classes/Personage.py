import pygame
from pygame.locals import *
from constants import *


class Personage:
    """This class create a personage"""

    def __init__(self, right, left, up, down, level):
        # Sprites du personnage
        self.right = pygame.image.load(right).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.up = pygame.image.load(up).convert_alpha()
        self.down = pygame.image.load(down).convert_alpha()
        # Position of the personnage in steps et pixels
        self.step_x = 0
        self.step_y = 0
        self.x = 0
        self.y = 0
        # Default direction
        self.direction = self.right
        # The level in wich the personnage is
        self.level = level

    def move(self, direction):
        """Method to move the personnage"""
        # Moving up
        if direction == 'right':
            # To stay within the window
            if self.step_x < (N_SPRITE_Y - 1):
                # We check that the destination step is not a wall
                if self.level.structure[self.step_y][self.step_x + 1] != 'w':
                    self.step_x += 1
                    # Calculate the realtime position in pixel
                    self.x = self.step_x * SPRITE_SIZE
                    # Save this path
                    self.level.mgpaths.append([self.x, self.y])
            # Image in the good direction
            self.direction = self.right

        # Move to the left
        if direction == 'left':
            if self.step_x > 0:
                if self.level.structure[self.step_y][self.step_x - 1] != 'w':
                    self.step_x -= 1
                    self.x = self.step_x * SPRITE_SIZE
                    self.level.mgpaths.append([self.x, self.y])
            self.direction = self.left

        # Move to up direction
        if direction == 'up':
            if self.step_y > 0:
                if self.level.structure[self.step_y - 1][self.step_x] != 'w':
                    self.step_y -= 1
                    self.y = self.step_y * SPRITE_SIZE
                    self.level.mgpaths.append([self.x, self.y])
            self.direction = self.up

        # Move downwards
        if direction == 'down':
            if self.step_y < (N_SPRITE_Y - 1):
                if self.level.structure[self.step_y + 1][self.step_x] != 'w':
                    self.step_y += 1
                    self.y = self.step_y * SPRITE_SIZE
                    self.level.mgpaths.append([self.x, self.y])
            self.direction = self.down
