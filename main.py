
import pygame
import os, sys
from pygame.locals import *     # Further explanation can be found at: https://www.pygame.org/docs/ref/locals.html#module-pygame.locals
pygame.init()

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Clock ticking for FPS (60fps)
clock = pygame.time.Clock()

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

# old code just incase for bg pygame.image.load(os.path.join("Assets/Backgrounds", "Inside_IESB.jpg")).convert()

# NOTE: The background will eventually be changed to a dictionary to compensate for different levels
# Backgrounds
main_menu_bg_img = pygame.image.load(os.path.join("Assets/Screens", "main menu.png"))
main_menu_bg = pygame.transform.scale(main_menu_bg_img, (1280, 720))

play_screen_bg_img = pygame.image.load(os.path.join("Assets/Screens", "play screen.png"))
play_screen_bg = pygame.transform.scale(play_screen_bg_img, (1280, 720))

level_select_bg_img = pygame.image.load(os.path.join("Assets/Screens", "level select.png"))
level_select_bg = pygame.transform.scale(level_select_bg_img, (1280, 720))

settinngs_bg_img = pygame.image.load(os.path.join("Assets/Screens", "settings screen.png"))
settings_bg = pygame.transform.scale(settinngs_bg_img, (1280, 720))

# main menu
def main_menu():
    click = False
    while True:

        # creating the background image
        WINDOW.fill((0, 0, 0))
        WINDOW.blit(main_menu_bg, (0, 0))

        # position of the mouse
        mx, my = pygame.mouse.get_pos()
        # print(mx, my)

        # invisible rectangles for the buttons
        button_1 = pygame.Rect(538, 272, 268, 97)
        button_2 = pygame.Rect(537, 408, 268, 97)
        button_3 = pygame.Rect(538, 545, 268, 97)
        button_4 = pygame.Rect(1214, 10, 51, 44)
        if button_1.collidepoint((mx, my)):
            if click:
                play_screen()
        if button_2.collidepoint((mx, my)):
            if click:
                level_select()
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        if button_4.collidepoint((mx, my)):
            if click:
                settings()
        # pygame.draw.rect(WINDOW, (255, 0, 0), button_1)
        # pygame.draw.rect(WINDOW, (255, 0, 0), button_2)
        # pygame.draw.rect(WINDOW, (255, 0, 0), button_3)
        # pygame.draw.rect(WINDOW, (255, 0, 0), button_4)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


# play screen
def play_screen():
    click = False
    run = True
    while run:

        WINDOW.fill((0, 0, 0))
        WINDOW.blit(play_screen_bg, (0, 0))

        mx, my = pygame.mouse.get_pos()
        # print(mx, my)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


# settings screen
def settings():
    click = False
    run = True
    while run:

        WINDOW.fill((0, 0, 0))
        WINDOW.blit(settings_bg, (0, 0))

        mx, my = pygame.mouse.get_pos()
        # print(mx, my)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


# level select screen
def level_select():
    click = False
    run = True
    while run:

        WINDOW.fill((0, 0, 0))
        WINDOW.blit(level_select_bg, (0, 0))

        mx, my = pygame.mouse.get_pos()
        # print(mx, my)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


# 
# game event Loop
def game():
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
        pygame.display.flip()

main_menu()

""" I started to work on some of the code for techie and what not, but I think im going to try and create a main menu first -John

    Okay, I did some research and it seems that putting each menu screen and the game itself into their own functions might be the way to go. 
        Working on them right now. -John"""
