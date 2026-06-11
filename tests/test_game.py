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

import pytest
from prog_flash.card import Card
from prog_flash.game import StudySessionController


def test_flip_card(
    study_session: StudySessionController,
    card: Card,
    capsys: pytest.CaptureFixture,
) -> None:
    assert study_session.is_front()
    study_session.flip_card()
    assert not study_session.is_front()
    card.view_card(study_session.is_front())
    out, _ = capsys.readouterr()
    assert out == f"{card.back}\n", "Should show back text after flipping."
