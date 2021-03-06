import pygame
import os, sys
from pygame.locals import *     # Further explanation can be found at: https://www.pygame.org/docs/ref/locals.html#module-pygame.locals
from random import randint
pygame.init()
pygame.mixer.init()


# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
DIFFICULTY = "easy"
last_level = "iesb"
game_speed = 20
i = 20
points = 0
obstacles = []
# Sound constants
jump_path = os.path.join("Sounds", "jump.wav")
jump_sound = pygame.mixer.Sound(jump_path)

bkg_path = os.path.join("Sounds", "bkg.mp3")
pygame.mixer.music.load(bkg_path)
pygame.mixer.music.play(-1)
  

# Clock ticking for FPS (60fps)
clock = pygame.time.Clock()


# Creating the window of the game
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("TechTime Racers") # Window name


# Techie "Animations"
techie_run = [pygame.image.load(os.path.join("Assets/Techie", "Techie Run Frame 1.PNG")).convert_alpha(), 
            pygame.image.load(os.path.join("Assets/Techie", "Techie Run Frame 2.PNG")).convert_alpha()]
techie_jump = pygame.image.load(os.path.join("Assets/Techie", "Techie Jump.PNG")).convert_alpha()
techie_duck = pygame.image.load(os.path.join("Assets/Techie", "Techie Duck.PNG")).convert_alpha()


# obstacles
arduino_png = [pygame.image.load(os.path.join("Assets/Obstacles", "Arduino 1.PNG")).convert_alpha(),
            pygame.image.load(os.path.join("Assets/Obstacles", "Arduino 2.PNG")).convert_alpha()]
sign_png = [pygame.image.load(os.path.join("Assets/Obstacles", "Stop Sign.PNG")).convert_alpha(),
            pygame.image.load(os.path.join("Assets/Obstacles", "Yield Sign.PNG")).convert_alpha()]
pn_table_png = [pygame.image.load(os.path.join("Assets/Obstacles", "Picnic Table 1.PNG")).convert_alpha(),
            pygame.image.load(os.path.join("Assets/Obstacles", "Picnic Table 2.PNG")).convert_alpha()]
squirrel_png = [pygame.image.load(os.path.join("Assets/Obstacles", "Squirrel 1.PNG")).convert_alpha(),
            pygame.image.load(os.path.join("Assets/Obstacles", "Squirrel 2.PNG")).convert_alpha()]
bird_png = [pygame.image.load(os.path.join("Assets/Obstacles", "Bird Fly 1.PNG")).convert_alpha(),
            pygame.image.load(os.path.join("Assets/Obstacles", "Bird Fly 2.PNG")).convert_alpha()]
books_png = [pygame.image.load(os.path.join("Assets/Obstacles", "Book 1.PNG")).convert_alpha(),
            pygame.image.load(os.path.join("Assets/Obstacles", "Book 2.PNG")).convert_alpha()]
football_ground_png = [pygame.image.load(os.path.join("Assets/Obstacles", "Football Ground.PNG")).convert_alpha(),
                    pygame.image.load(os.path.join("Assets/Obstacles", "Football Ground.PNG")).convert_alpha()]
football_air_png = [pygame.image.load(os.path.join("Assets/Obstacles", "Football Air.PNG")).convert_alpha(), 
                pygame.image.load(os.path.join("Assets/Obstacles", "Football Air.PNG")).convert_alpha()]


# Class for Techie, playable character
class Player:
    x_pos = 100
    y_pos = 390
    y_pos_duck = 470
    static_jump_vel = 8.5

    def __init__(self):
        self.run_png = techie_run
        self.jump_png = techie_jump
        self.duck_png = techie_duck

        self.isRun = True
        self.isJump = False
        self.isDuck = False

        self.step_index = 0
        self.dynamic_jump_vel = self.static_jump_vel
        self.image = self.run_png[0]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.x_pos
        self.player_rect.y = self.y_pos

    # used to check the status of the player and what is happening
    def update(self, user_input):
        if self.isRun:
            self.run()
        if self.isJump:
            self.jump()
        if self.isDuck:
            self.duck()

        if self.step_index >= 10:
            self.step_index = 0
        
        if user_input[pygame.K_UP] and not self.isJump:
            self.isRun = False
            self.isJump = True
            pygame.mixer.Sound.play(jump_sound)
            self.isDuck = False
        elif user_input[pygame.K_DOWN] and not self.isJump:
            self.isRun = False
            self.isJump = False
            self.isDuck = True
        elif not (self.isJump or user_input[pygame.K_DOWN]):
            self.isRun = True
            self.isJump = False
            self.isDuck = False

    # running logic
    def run(self):
        self.image = self.run_png[self.step_index // 5]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.x_pos
        self.player_rect.y = self.y_pos
        self.step_index += 1
    
    # jumping logic
    def jump(self):
        self.image = self.jump_png
        if self.isJump:
            self.player_rect.y -= self.dynamic_jump_vel * 8
            self.dynamic_jump_vel -= 0.65
        if self.dynamic_jump_vel < - self.static_jump_vel:
            self.isJump = False
            self.dynamic_jump_vel = self.static_jump_vel
    
    # jumping logic
    def duck(self):
        self.image = self.duck_png
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.x_pos
        self.player_rect.y = self.y_pos_duck
        self.step_index += 1

    # drawing Techie on the screen
    def draw(self, WINDOW):
        WINDOW.blit(self.image, (self.player_rect.x, self.player_rect.y))


# class for every obstacle to inherit from
class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = WINDOW_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
    
    def draw(self, WINDOW):
        WINDOW.blit(self.image[self.type], self.rect)


class Arduino(Obstacle):
    def __init__(self, image):
        self.type = randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 500


class Sign(Obstacle):
    def __init__(self, image):
        self.type = randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 385


class Books(Obstacle):
    def __init__(self, image):
        self.type = randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 450


class PicnicTable(Obstacle):
    def __init__(self, image):
        self.type = randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 500


class Squirrel(Obstacle):
    def __init__(self, image):
        self.type = randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 480


class FootballGround(Obstacle):
    def __init__(self, image):
        self.type = randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 500


class FootballAir(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 350
        self.index = 0
    
    def draw(self, WINDOW):
        if self.index >= 9:
            self.index = 0
        WINDOW.blit(self.image[self.index//5], self.rect)


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 300
        self.index = 0
    
    def draw(self, WINDOW):
        if self.index >= 9:
            self.index = 0
        WINDOW.blit(self.image[self.index//5], self.rect)


# Backgrounds
main_menu_bg_img = pygame.image.load(os.path.join("Assets/Screens", "main menu.png")).convert_alpha()
main_menu_bg = pygame.transform.scale(main_menu_bg_img, (1280, 720))

play_screen_bg_img = pygame.image.load(os.path.join("Assets/Screens", "play screen.png")).convert_alpha()
play_screen_bg = pygame.transform.scale(play_screen_bg_img, (1280, 720))

level_select_bg_img = pygame.image.load(os.path.join("Assets/Screens", "level select.png")).convert_alpha()
level_select_bg = pygame.transform.scale(level_select_bg_img, (1280, 720))

settinngs_bg_img = pygame.image.load(os.path.join("Assets/Screens", "settings screen.png")).convert_alpha()
settings_bg = pygame.transform.scale(settinngs_bg_img, (1280, 720))

<<<<<<< HEAD
# Background Music
#def music():
  #  music_file = "bkg.mp3"
   # pygame.mixer.init()
   # pygame.mixer.music.load(music_file)
   #pygame.mixer.music.play(-1)

=======
>>>>>>> 56922f87b2ac2c99aa56e35b0f7fd008f57f01d2

# level dictionary
# the list contains path for [background, foreground, obstacles]
lvls_dict = {
    "iesb": ["Outside_IESB.png", "Road.PNG", arduino_png],
    "bogard": ["Bogard.png", "Road.PNG", sign_png],
    "clock": ["Clock_Tower.png", "Brick.PNG", pn_table_png],
    "lotm": ["Lady_of_Mist.png", "Brick.PNG", squirrel_png],
    "wyly": ["Wyly.png", "Brick.PNG", books_png],
    "endless": ["The_Joe.png", "Grass.PNG", football_ground_png]}


# Sound

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
                    settings()
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
<<<<<<< HEAD
        # play music
       # music()

=======
>>>>>>> 56922f87b2ac2c99aa56e35b0f7fd008f57f01d2
        # draw background
        WINDOW.blit(play_screen_bg, (0, 0))

        # get position of mouse
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
    global i, game_speed
    global DIFFICULTY
    click = False
    run = True
    while run:

        # draw background
        WINDOW.blit(settings_bg, (0, 0))

        # get position of mouse
        mx, my = pygame.mouse.get_pos(292, 354, 269, 98)
        # print(mx, my)

        # invisible buttons
        easy_button = pygame.Rect(520, 232, 270, 99)
        medium_button = pygame.Rect(520, 376, 270, 99)
        hard_button = pygame.Rect(520, 518, 270, 99)
        back_button = pygame.Rect(11, 8, 33, 34)
        menu_button = pygame.Rect(1186, 7, 85, 32)

        # button functions
        if easy_button.collidepoint((mx, my)):
            if click:
                DIFFICULTY = "easy"
                i = 20
                game_speed = 20
                run = False
        if medium_button.collidepoint((mx, my)):
            if click:
                DIFFICULTY = "medium"
                i = 30
                game_speed = 30
                run = False
        if hard_button.collidepoint((mx, my)):
            if click:
                DIFFICULTY = "hard"
                i = 40
                game_speed = 40
                run = False
        if back_button.collidepoint((mx, my)):
            if click:
                run = False
        if menu_button.collidepoint((mx, my)):
            if click:
                main_menu()
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
        # pygame.draw.rect(WINDOW, (0, 255, 0), menu_button)

        pygame.display.update()
        clock.tick(60)


# level select screen
def level_select():
    click = False
    run = True
    while run:

        # draw background
        WINDOW.blit(level_select_bg, (0, 0))

        # get position of mouse
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
    global points, obstacles, i, game_speed
    
    # creating the player
    techie = Player()

    # i is used to move the screen
    i = game_speed

    # used to keep score
    points = 0
    font = pygame.font.Font("freesansbold.ttf", 20)
    def score():
        global points
        points += 1
        point_display = font.render(f"Points: {points}", True, (0, 0, 0))
        pd_rect = point_display.get_rect()
        pd_rect.center = (1200, 30)
        WINDOW.blit(point_display, pd_rect)


    # background
    bg_img = pygame.image.load(os.path.join("Assets/Backgrounds", lvls_dict[level_key][0])).convert_alpha()
    bg = pygame.transform.scale(bg_img, (1280, 720))

    # foreground
    fg_img = pygame.image.load(os.path.join("Assets/Foreground", lvls_dict[level_key][1])).convert_alpha()
    fg = pygame.transform.scale(fg_img, (1280, 570))

    run = 1
    while run:
        timer = pygame.time.Clock()

        counter, text = 120, '120'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont('Consolas', 30)

        run = True
        font = pygame.font.Font("freesansbold.ttf", 20)
        while run:
            for e in pygame.event.get():
                if e.type == pygame.USEREVENT:
                    counter -= 1
                    text = str(counter).rjust(3) if counter > 0 else 'Congrats, you completed the level!'
                if e.type == pygame.QUIT:
                    run = False
            point_display = font.render(f"Time: {timer}", True, (0, 0, 0))
            pd_rect = point_display.get_rect()
            pd_rect.center = (1000, 30)
            WINDOW.blit(point_display, pd_rect)

        # drawing the bg
        WINDOW.fill((0, 0, 0))
        WINDOW.blit(bg, (i, 0))
        WINDOW.blit(bg, (WINDOW_WIDTH + i, 0))

        #drawing the fg
        WINDOW.blit(fg, (0, 150))
        WINDOW.blit(fg, (i, 150))
        WINDOW.blit(fg, (WINDOW_WIDTH + i, 150))

        # moving the bg & fg
        if i <= -WINDOW_WIDTH:
            WINDOW.blit(bg, (WINDOW_WIDTH + i, 0))
            WINDOW.blit(fg, (WINDOW_WIDTH + i, 150))
            i = 0
        
        # speed at which bg moves
        i -= game_speed

        # fps
        clock.tick(60)

        # checking for quit or pause game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    obstacles.pop()
                    settings()
        
        # increment score
        score()

        # grabbing input for Player class
        user_input = pygame.key.get_pressed()

        # drawing player
        techie.draw(WINDOW)
        techie.update(user_input)

        # creating obstacles according to level
        if len(obstacles) == 0:
            if level_key == "iesb":
                obstacles.append(Arduino(lvls_dict[level_key][2]))
            elif level_key == "bogard":
                obstacles.append(Sign(lvls_dict[level_key][2]))
            elif level_key == "clock":
                obstacles.append(PicnicTable(lvls_dict[level_key][2]))
            elif level_key == "lotm":
                if randint(0, 1) == 0:
                    obstacles.append(Squirrel(lvls_dict[level_key][2]))
                else:
                    obstacles.append(Bird(bird_png))
            elif level_key == "wyly":
                if randint(0, 1) == 0:
                    obstacles.append(Books(lvls_dict[level_key][2]))
                else:
                    obstacles.append(Bird(bird_png))
            elif level_key == "endless":
                if randint(0, 1) == 0:
                    obstacles.append(FootballGround(lvls_dict[level_key][2]))
                else:
                    obstacles.append(FootballAir(football_air_png))

        # drawing obstacle and hit detection
        for obstacle in obstacles:
            obstacle.draw(WINDOW)
            obstacle.update()

            # used to show hitboxes
            pygame.draw.rect(WINDOW, (255, 0, 0), techie.player_rect, 2)
            pygame.draw.rect(WINDOW, (255, 0, 0), obstacle.rect, 2)

            # checking for collision of hitboxes
            if techie.player_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                obstacles.pop()
                run = 0

        pygame.display.update()

main_menu()

"""Idea for end level implementation. Maybe have an if condition with the points??? Ill try to figure out a better way later -John"""
"""Need to add a start_event and end_event for the levels"""
"""Need to figure out how to "continue" """
