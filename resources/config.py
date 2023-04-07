#########################################
# Global Configuration Variables        #
# import anywhere you need these vars   #
#########################################
import pygame

from resources.game_properties import GameProperties

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
