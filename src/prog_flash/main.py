# Copyright (C) 2026 K Law All rights reserved.
# Licensed under the GPLv3.


from prog_flash.card import Card
from prog_flash.game import GameLogicController


def process_card_command(command: str, game_session: GameLogicController, card: Card):
    match command:
        case 'f':
            game_session.flip_card()
        case 'q':
            print('Good job studying')
            exit()
        case 'm':
            card.mark_correct()
        case 'help':
            print('Press "f" to flip card')
            print('Press "q" to quit')


def main() -> None:
    game_session = GameLogicController()
    card = Card('Front of card', 'Back of Card')

    while True:
        side = game_session.disp_front
        print(card.get_side(side))
        print('Enter command type "help" for help.')
        command: str = input()
        process_card_command(command, game_session, card)


if __name__ == '__main__':
    main()
