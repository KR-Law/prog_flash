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
from typing import Optional


class Card:
    def __init__(self, front: str, back: str, updated_at: Optional[datetime] = None):
        self.front: str = front
        self.back: str = back
        self.marked: bool = False
        self.updated_at: datetime = updated_at or datetime.now(timezone.utc)
        ## Transient Functions
        self.dsp_side: str = "front"

    def _touch(self) -> None:
        self.updated_at = datetime.now(timezone.utc)

    def view_card(self):
        print(self.front) if self.dsp_side == "front" else print(self.back)

    def flip_card(self) -> None:
        if self.dsp_side == "front":
            self.dsp_side = "back"
        else:
            self.dsp_side = "front"

    def mark_card(self) -> None:
        self.marked = not self.marked
        self._touch()
