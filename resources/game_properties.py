from typing import Final


class GameProperties:

    WINDOW_NAME: Final = "Duran Games"
    WINDOW_WIDTH: Final = 1000
    WINDOW_HEIGHT: Final = 800
    FRAMES_PER_SECOND: Final = 20
    PLAYER_VELOCITY: Final = 5

    # initialize the object
    def __init__(self):
        print("Sourcing game properties")

    # overwrite the toString of this object
    def __str__(self):
        return f"""GameProperties(
               {self.WINDOW_NAME}
               {self.WINDOW_WIDTH}
               {self.WINDOW_HEIGHT}
               {self.FRAMES_PER_SECOND}
               {self.PLAYER_VELOCITY}
                )"""

