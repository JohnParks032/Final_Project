
import pygame
import os, sys
from pygame.locals import *     # Further explanation can be found at: https://www.pygame.org/docs/ref/locals.html#module-pygame.locals
pygame.init()

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
DIFFICULTY = "easy"
last_level = "iesb"

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

# Backgrounds
main_menu_bg_img = pygame.image.load(os.path.join("Assets/Screens", "main menu.png"))
main_menu_bg = pygame.transform.scale(main_menu_bg_img, (1280, 720))

play_screen_bg_img = pygame.image.load(os.path.join("Assets/Screens", "play screen.png"))
play_screen_bg = pygame.transform.scale(play_screen_bg_img, (1280, 720))

level_select_bg_img = pygame.image.load(os.path.join("Assets/Screens", "level select.png"))
level_select_bg = pygame.transform.scale(level_select_bg_img, (1280, 720))

settinngs_bg_img = pygame.image.load(os.path.join("Assets/Screens", "settings screen.png"))
settings_bg = pygame.transform.scale(settinngs_bg_img, (1280, 720))

# level dictionary
# the list contains path for [background, foreground, obstacles, flying obstacles]
lvls_dict = {
    "iesb": ["Outside_IESB.png", "Road.PNG"],
    "bogard": ["Inside_IESB.png", "Road.PNG"],
    "clock": ["Clock_Tower.png", "Brick.PNG"],
    "lotm": ["Lady_of_Mist.png", "Brick.PNG"],
    "wyly": ["Wyly.png", "Brick.PNG"],
    "endless": ["The_Joe.png", "Grass.PNG"]
}

# main menu
def main_menu():
    click = False
    while True:

        # creating the background image
        WINDOW.blit(main_menu_bg, (0, 0))

        # position of the mouse
        mx, my = pygame.mouse.get_pos()

        # used to find position of mouse, helps define rectangle parameters
        # print(mx, my)

        # invisible rectangles for the buttons
        play_button = pygame.Rect(538, 272, 268, 97)
        level_select_button = pygame.Rect(537, 408, 268, 97)
        quit_button = pygame.Rect(538, 545, 268, 97)
        settings_button = pygame.Rect(1214, 10, 51, 44)

        # button functions
        if play_button.collidepoint((mx, my)):
            if click:
                play_screen()
        if level_select_button.collidepoint((mx, my)):
            if click:
                level_select()
        if quit_button.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        if settings_button.collidepoint((mx, my)):
            if click:
                settings()

        # used to draw rectangles to see their position
        # pygame.draw.rect(WINDOW, (255, 0, 0), button_1)
        # pygame.draw.rect(WINDOW, (255, 0, 0), button_2)
        # pygame.draw.rect(WINDOW, (255, 0, 0), button_3)
        # pygame.draw.rect(WINDOW, (255, 0, 0), button_4)

        # check for clicks or button push
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

        WINDOW.blit(play_screen_bg, (0, 0))

        mx, my = pygame.mouse.get_pos()
        # print(mx, my)

        # invisible buttons
        new_game_button = pygame.Rect(292, 354, 269, 98)
        continue_button = pygame.Rect(719, 354, 269, 98)
        back_button = pygame.Rect(9, 6, 33, 34)

        # button functions
        if new_game_button.collidepoint((mx, my)):
            if click:
                game("iesb")
        if continue_button.collidepoint((mx, my)):
            if click:
                game(last_level)
        if back_button.collidepoint((mx, my)):
            if click:
                run = False

        # check for clicks or button push
        click = False
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

        # used to draw rectangles to see their position
        # pygame.draw.rect(WINDOW, (255, 0, 0), new_game_button)
        # pygame.draw.rect(WINDOW, (255, 0, 0), continue_button)
        # pygame.draw.rect(WINDOW, (0, 255, 0), back_button)

        pygame.display.update()
        clock.tick(60)


# settings screen
def settings():
    global DIFFICULTY
    click = False
    run = True
    while run:

        WINDOW.blit(settings_bg, (0, 0))

        mx, my = pygame.mouse.get_pos(292, 354, 269, 98)
        # print(mx, my)

        # invisible buttons
        easy_button = pygame.Rect(520, 232, 270, 99)
        medium_button = pygame.Rect(520, 376, 270, 99)
        hard_button = pygame.Rect(520, 518, 270, 99)
        back_button = pygame.Rect(11, 8, 33, 34)

        # button functions
        if easy_button.collidepoint((mx, my)):
            if click:
                DIFFICULTY = "easy"
                run = False
        if medium_button.collidepoint((mx, my)):
            if click:
                DIFFICULTY = "medium"
                run = False
        if hard_button.collidepoint((mx, my)):
            if click:
                DIFFICULTY = "hard"
                run = False
        if back_button.collidepoint((mx, my)):
            if click:
                run = False

        # check for clicks or button push
        click = False
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

        # draw rects
        # pygame.draw.rect(WINDOW, (255, 0, 0), easy_button)
        # pygame.draw.rect(WINDOW, (255, 0, 0), medium_button)
        # pygame.draw.rect(WINDOW, (255, 0, 0), hard_button)
        # pygame.draw.rect(WINDOW, (0, 255, 0), back_button)

        pygame.display.update()
        clock.tick(60)


# level select screen
def level_select():
    click = False
    run = True
    while run:

        WINDOW.blit(level_select_bg, (0, 0))

        mx, my = pygame.mouse.get_pos()
        # print(mx, my)

        # invisible buttons
        lvl_iesb_button = pygame.Rect(211, 296, 270, 99)
        lvl_bogard_button = pygame.Rect(534, 296, 270, 99)
        lvl_clock_button = pygame.Rect(875, 296, 270, 99)
        lvl_lotm_button = pygame.Rect(211, 490, 270, 99)
        lvl_wyly_button = pygame.Rect(534, 490, 270, 99)
        lvl_endless_button = pygame.Rect(875, 490, 270, 99)
        back_button = pygame.Rect(4, 5, 33, 34)

        # button functions
        if lvl_iesb_button.collidepoint((mx, my)):
            if click:
                game("iesb")
        if lvl_bogard_button.collidepoint((mx, my)):
            if click:
                game("bogard")
        if lvl_clock_button.collidepoint((mx, my)):
            if click:
                game("clock")
        if lvl_lotm_button.collidepoint((mx, my)):
            if click:
                game("lotm")
        if lvl_wyly_button.collidepoint((mx, my)):
            if click:
                game("wyly")
        if lvl_endless_button.collidepoint((mx, my)):
            if click:
                game("endless")
        if back_button.collidepoint((mx, my)):
            if click:
                run = False

        # check for clicks or button push
        click = False
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

        # draw rects
        # pygame.draw.rect(WINDOW, (255, 0, 0), lvl_iesb_button)
        # pygame.draw.rect(WINDOW, (255, 0, 0), lvl_bogard_button)
        # pygame.draw.rect(WINDOW, (255, 0, 0), lvl_clock_button)
        # pygame.draw.rect(WINDOW, (255, 0, 0), lvl_lotm_button)
        # pygame.draw.rect(WINDOW, (255, 0, 0), lvl_wyly_button)
        # pygame.draw.rect(WINDOW, (255, 0, 0), lvl_endless_button)
        # pygame.draw.rect(WINDOW, (255, 0, 0), back_button)

        pygame.display.update()
        clock.tick(60)


# game event Loop
def game(level_key):
    # i is used to move the screen
    i = 0
    run = True
    while run:
        
        # background
        bg_img = pygame.image.load(os.path.join("Assets/Backgrounds", lvls_dict[level_key][0]))
        bg = pygame.transform.scale(bg_img, (1280, 720))

        # foreground
        fg_img = pygame.image.load(os.path.join("Assets/Foreground", lvls_dict[level_key][1]))
        fg = pygame.transform.scale(fg_img, (1280, 570))

        # drawing the bg
        WINDOW.fill((0, 0, 0))
        WINDOW.blit(bg, (i, 0))
        WINDOW.blit(bg, (WINDOW_WIDTH + i, 0))

        #drawing the fg
        WINDOW.blit(fg, (0, 150))
        WINDOW.blit(fg, (i, 150))
        WINDOW.blit(fg, (WINDOW_WIDTH + i, 150))

        # moving the bg & fg
        if i == -WINDOW_WIDTH:
            WINDOW.blit(bg, (WINDOW_WIDTH + i, 0))
            WINDOW.blit(fg, (WINDOW_WIDTH + i, 150))
            i = 0

        i -= 10

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False

        pygame.display.update()

main_menu()

""" I started to work on some of the code for techie and what not, but I think im going to try and create a main menu first -John

    Okay, I did some research and it seems that putting each menu screen and the game itself into their own functions might be the way to go. 
        Working on them right now. -John
        
    The menus are now finished!! -John"""
