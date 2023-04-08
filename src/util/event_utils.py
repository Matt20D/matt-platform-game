from src.classes.Player import Player


class EventUtils:

    @staticmethod
    def handle_character_choice() -> Player:

        # TODO uncomment when ready...

        # character_input = input("Which main character would you like to use?").strip()

        # if character_input not in Player.AVAILABLE_PLAYERS:
        #     return Player(100, 100, 50, 50, "NinjaFrog")

        # return Player(100, 100, 50, 50, character_input)

        return Player(100, 100, 50, 50, "NinjaFrog")
