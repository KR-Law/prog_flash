# Copyright (C) 2026 K Law All rights reserved.
# Licensed under the GPLv3.


from prog_flash.card import Card
from prog_flash.game import StudySessionController


def process_card_command(
    command: str, game_session: StudySessionController, card: Card
):
    match command:
        case "f":
            game_session.flip_card()
        case "q":
            print("Good job studying")
            exit()


def main() -> None:

    game_session = StudySessionController()

    card = Card("Front of card", "Back of Card")
    print('Enter command type "help" for help.')
    command: str = input()
    process_card_command(command, game_session, card)


if __name__ == "__main__":
    main()
