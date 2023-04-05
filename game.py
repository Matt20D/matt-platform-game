#################################################
# Matt Duran's first game                       #
# Super Mario Bro's like platform game          #
# First commit: 4/3/2023                        #
#################################################

import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

# Game Source Code
from resources.game_properties import GameProperties
from src.util.background_utils import BackgroundUtils
from src.classes.Player import Player

# initialize the pygame module
pygame.init()

# set the caption for top of the window
pygame.display.set_caption(GameProperties.WINDOW_NAME)

# Depends on the size of the screen
WIDTH, HEIGHT = GameProperties.WINDOW_WIDTH, GameProperties.WINDOW_HEIGHT
FPS = GameProperties.FRAMES_PER_SECOND

# Speed that player moves on the screen
PLAYER_VELOCITY = GameProperties.FRAMES_PER_SECOND

game_window = pygame.display.set_mode((WIDTH, HEIGHT))


# This will handle our event loop
def main(window):
    clock = pygame.time.Clock()
    background, bg_image = BackgroundUtils.get_background("Blue.png", WIDTH, HEIGHT)

    player = Player(100, 100, 50, 50)

    run = True
    while run:

        # This guarantees that the game runs at a consistent rate
        # Slower computer then slower FPS
        clock.tick(FPS)

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                print(f"User has quit the game")
                run = False
                break

        # allow for continual movement of the frame
        player.loop(FPS)
        Player.handle_move(player, PLAYER_VELOCITY)

        # draw the full background
        BackgroundUtils.draw(window, background, bg_image, player)

    pygame.quit()
    # quit()


if __name__ == "__main__":
    print("~~~Starting the platform game~~~")

    main(game_window)

    print("~~~Ending the platform game~~~")
