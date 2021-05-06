
import pygame
import os, sys
from pygame.locals import *     # Further explanation can be found at: https://www.pygame.org/docs/ref/locals.html#module-pygame.locals
pygame.init()

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720


# Creating the window of the game
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("TechTime Racers") # Window name


# Class for Techie, playable character
class Player(pygame.sprite.Sprite):
    run = [pygame.image.load(os.path.join("Assets/"))]
    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        

# Background
# NOTE: The background will eventually be changed to a dictionary to compensate for different levels
bg = pygame.Surface(WINDOW.get_size())
bg = bg.convert()
bg.fill((250, 250, 250))


# Main Event Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

