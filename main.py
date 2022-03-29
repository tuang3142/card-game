# 1 - Import packages
import pygame
from pygame.locals import *
import pygwidgets
import sys
from game import *

# 2 - Define constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
FRAMES_PER_SECOND = 30


def main():
    # 3 - Initialize the environment
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    # 4 - Load assets: image(s), sound(s),  etc.
    background = pygwidgets.Image(window, (0, 0),
                                  'assets/images/background.png')
    new_game_button = pygwidgets.TextButton(window, (20, 530),
                                            'New Game', width=100, height=45)
    higher_button = pygwidgets.TextButton(window, (540, 520),
                                          'Higher', width=120, height=55)
    lower_button = pygwidgets.TextButton(window, (340, 520),
                                         'Lower', width=120, height=55)
    quit_button = pygwidgets.TextButton(window, (880, 530),
                                        'Quit', width=100, height=45)

    # 5 - Initialize variables
    game = Game(window)

    # 6 - Loop forever
    while True:
        # 7 - Check for and handle events
        for event in pygame.event.get():
            # close button or escape or quit button
            if event.type == pygame.QUIT or \
               event.type == KEYDOWN and event.key == K_ESCAPE or \
               quit_button.handleEvent(event):
                pygame.quit()
                sys.exit()
            if new_game_button.handleEvent(event):
                game.reset()
                lower_button.enable()
                higher_button.enable()
            game_over = higher_button.handleEvent(event) and game.evaluate_guess('higher') or \
                        lower_button.handleEvent(event) and game.evaluate_guess('lower')
            if game_over:
                higher_button.disable()
                lower_button.disable()

        # 8 - Do any "per frame" actions

        # 9 - Clear the window
        background.draw()

        # 10 - Draw all window elements
        game.draw()
        new_game_button.draw()
        higher_button.draw()
        lower_button.draw()
        quit_button.draw()

        # 11 - Update the window
        pygame.display.update()

        # 12 - Slow things down a bit
        clock.tick(FRAMES_PER_SECOND)  # make pygame wait


if __name__ == '__main__':
    main()
