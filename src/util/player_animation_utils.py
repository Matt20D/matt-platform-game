from resources.config import *
from os import listdir
from os.path import isfile, join


class PlayerAnimationUtils:

    @staticmethod
    def flip(sprites):
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

    @staticmethod
    def load_sprite_sheets(dir1, dir2, width, height, direction=False):
        """
        Load the sprite sheets for our character. falling, jump, etc.

        :param dir1:
        :param dir2:
        :param width: of image
        :param height: of image
        :param direction: do we need to load multiple directions. Flip
                          if equal to true
        :return:
        """

        path = join("assets", dir1, dir2)
        images = [file for file in listdir(path) if isfile(join(path, file))]

        all_sprites = {}

        for image in images:

            # load the sheet, and have transparent background
            sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

            sprites = []
            for i in range(sprite_sheet.get_width() // width):
                surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)

                # we want to create a surface that is the size of the desired animation
                # frame. i.e. the sprite animation.
                # Then draw it onto the surface
                # where in the image (Sprite sheet) do we want to take an individual image from and blit it
                # onto the surface. We aare grabbing an image frame.
                # blit means draw
                rect = pygame.Rect(i * width, 0, width, height)
                surface.blit(sprite_sheet, (0, 0), rect)
                sprites.append(pygame.transform.scale2x(surface))

            # we will need these directions if we would like to have multiple directions
            # for each animation.
            if direction:
                all_sprites[image.replace(".png", "") + "_right"] = sprites
                all_sprites[image.replace(".png", "") + "_left"] = PlayerAnimationUtils.flip(sprites)
            else:
                all_sprites[image.replace(".png", "")] = sprites

        return all_sprites
