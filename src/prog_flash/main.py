# Copyright (C) 2026 K Law
#
# This file is part of prog_flash.
#
# prog_flash is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# prog_flash is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with prog_flash.  If not, see <https://www.gnu.org/licenses/>.


from prog_flash.card import Card


def process_card_command(command, card: Card):
    match command:
        case "f":
            card.flip_card()
        case "q":
            print("Good job studying")
            exit()


def main() -> None:
    card = Card("Front of card", "Back of Card")
    print('Enter command type "help" for help.')
    command = input()
    process_card_command(command, card)


if __name__ == "__main__":
    main()
