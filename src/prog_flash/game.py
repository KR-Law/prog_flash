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


class StudySessionController:
    def __init__(self) -> None:
        self.disp_front: bool = True
        self.currentIndex: int = 0

    def flip_card(self):
        self.disp_front = not self.disp_front

    def is_front(self) -> bool:
        return self.disp_front
