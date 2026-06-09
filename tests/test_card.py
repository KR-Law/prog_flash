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


class TestCard:
    def setup_method(self):
        self.front_data = "Front of Card"
        self.back_data = "Back of Card"
        self.card = Card(self.front_data, self.back_data)

    def test_card_initialization(self):
        assert self.card.front == "Front of Card"
        assert self.card.back == "Back of Card"

    def test_view_card_side(
        self, capsys: CaptureFixture, monkeypatch: MonkeyPatch
    ) -> None:
        monkeypatch.setattr("builtins.input", lambda: None)
        self.card.view_card()
        out, _ = capsys.readouterr()
        assert out == f'{self.card.front}\nEnter command type "help" for help.\n'
