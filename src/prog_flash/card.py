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


class Card:
    def __init__(self, front: str, back: str):
        self.front: str = front
        self.back: str = back

    def get_command(self):
        print('Enter command type "help" for help.')
        command: str = input()
        return command

    def view_card(self):
        print(self.front)
        self.get_command()
