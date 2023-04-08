#################################################
# Matt Duran's first game                       #
# Super Mario Bro's like platform game          #
# First commit: 4/3/2023                        #
#################################################

# Game Source Code
from resources.config import *
from src.util.background_utils import BackgroundUtils
from src.util.event_utils import EventUtils
from src.classes.Player import Player


# This will handle our event loop
def main(window):
    clock = pygame.time.Clock()
    background, bg_image = BackgroundUtils.get_background("Blue.png", WIDTH, HEIGHT)

    player = EventUtils.handle_character_choice()

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
