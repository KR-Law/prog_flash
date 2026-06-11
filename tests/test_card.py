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


from pytest import MonkeyPatch, CaptureFixture
from prog_flash.card import Card
from datetime import datetime, timezone


class TestCard:
    def setup_method(self):
        db_row = {
            "front": "What is Python?",
            "back": "A programming language.",
            "updated_at": datetime(2026, 6, 9, 12, 0, 0, tzinfo=timezone.utc),
        }
        self.card = Card(**db_row)

    def test_card_initialization(self):
        assert self.card.front == "What is Python?"
        assert self.card.back == "A programming language."

    def test_view_card(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        monkeypatch.setattr("builtins.input", lambda: None)

        # 1. Test initial view (Front side)
        self.card.dsp_side = "front"
        self.card.view_card()
        out, _ = capsys.readouterr()
        assert out == f"{self.card.front}\n", "Should show front text on initial view."

        # 2. Flip the card to back side
        self.card.flip_card()
        assert self.card.dsp_side == "back"

        # 3. Test view after flipping (Back side)
        self.card.view_card()
        out, _ = capsys.readouterr()
        assert out == f"{self.card.back}\n", "Should show back text after flipping."

    def test_flip_card(self) -> None:
        side = self.card.dsp_side
        print(side)
        self.card.flip_card()
        assert self.card.dsp_side == "back"

    def test_mark(self) -> None:
        self.card.mark_card()
        assert self.card.marked

        self.card.mark_card()
        assert not self.card.marked
