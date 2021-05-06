
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
    run = [pygame.image.load(os.path.join("Assets/Techie", "Techie Run Frame 1.png")), 
            pygame.image.load(os.path.join("Assets/Techie", "Techie Run Frame 2.png"))]
    jump = pygame.image.load(os.path.join("Assets/Techie", "Techie Jump.png"))
    duck = pygame.image.load(os.path.join("Assets/Techie", "Techie Duck.png"))
    def __init__(self, width, height, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()

# Display dictionary

# Background
# NOTE: The background will eventually be changed to a dictionary to compensate for different levels
bg = pygame.image.load(os.path.join("Assets/Backgrounds", "Inside_IESB.jpg")).convert()

# Clock ticking for FPS (60fps)
clock = pygame.time.Clock()

# Main Event Loop
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    pygame.display.flip()

""" I started to work on some of the code for techie and what not, but I think im going to try and create a main menu first -John"""