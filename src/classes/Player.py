import pygame
from typing import Final

class Player(pygame.sprite.Sprite):
    """
    This player class inherits from pygame.sprite.Sprite
    """

    COLOR: Final = (255, 0, 0)
    GRAVITY: Final = 1

    def __init__(self, x, y, width, height):

        # this rect allows us to do collisions between our
        # sprites
        self.rect = pygame.Rect(x, y, width, height)

        # allows us to do jumping and running
        self.x_vel = 0
        self.y_vel = 0

        self.mask = None
        self.direction = "left"
        self.animation_count = 0

        self.fall_time = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel

        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel

        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def move_up(self, vel):
        ...

    def move_down(self, vel):
        ...

    def loop(self, fps):
        self.y_vel += min(1, self.calc_gravity_acceleration(fps))
        self.move(self.x_vel, self.y_vel)

        self.fall_time += 1

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)

    def calc_gravity_acceleration(self, fps):

        return (self.fall_time / fps) * self.GRAVITY

    @staticmethod
    def handle_move(player, velocity):

        keys = pygame.key.get_pressed()

        player.x_vel = 0
        if keys[pygame.K_LEFT]:
            player.move_left(velocity)
        if keys[pygame.K_RIGHT]:
            player.move_right(velocity)
