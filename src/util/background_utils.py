import pygame
from os.path import isfile, join


class BackgroundUtils:

    @staticmethod
    def get_background(name: str, window_width: int, window_height: int) -> tuple:
        """
        Determine tile locations, and the loaded image.

        :param window_height:
        :param window_width:
        :param name: of tile color
        :return: tuple(tiles: list, image: loaded_image
        """

        # loaded image by filename
        loaded_image = pygame.image.load(join("assets", "Background", name))

        # get image width and height
        _, _, width, height = loaded_image.get_rect()

        # store i,j coord for where to begin drawing the tiles
        tiles = []

        # always want to start drawing tile at upper left hand side
        for i in range(window_width // width + 1):
            for j in range(window_height // height + 1):
                tile_upper_lhs = (i * width, j * height)
                tiles.append(tile_upper_lhs)

        return tiles, loaded_image

    @staticmethod
    def draw(window, background_tile_locations, bg_image, player) -> None:
        """
        Draws the background image into the window at each
        tile location.

        :param player: to display
        :param window: game_window
        :param background_tile_locations: list of i,j coord of where to draw
        :param bg_image: loaded tile image object
        :return: None
        """

        for tile_loc in background_tile_locations:
            window.blit(bg_image, tile_loc)

        player.draw(window)

        pygame.display.update()
