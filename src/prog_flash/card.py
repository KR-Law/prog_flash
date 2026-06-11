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


from datetime import datetime, timezone


class Card:
    def __init__(self, front: str, back: str) -> None:
        self.front: str = front
        self.back: str = back
        self.marked: bool = False
        self.created_at: datetime = datetime.now(timezone.utc)
        self.updated_at: datetime = self.created_at
        self.viewed_at: datetime = self.created_at

    def _touch(self) -> None:
        self.updated_at = datetime.now(timezone.utc)

    def view_card(self, is_front) -> None:
        print(self.front) if is_front else print(self.back)

    def mark_card(self) -> None:
        self.marked = not self.marked
        self._touch()

    def update_card(self, front: str, back: str) -> None:
        self.front = front
        self.back = back
        self._touch()
