# Copyright (C) 2026 K Law All rights reserved.
# Licensed under the GPLv3.

import pytest
from prog_flash.card import Card
from prog_flash.game import StudySessionController


def test_flip_back_front_to_back(
    study_session: StudySessionController,
    card: Card,
    capsys: pytest.CaptureFixture,
) -> None:
    assert study_session.is_front()
    study_session.flip_card()
    assert not study_session.is_front()
    card.view_side(study_session.is_front())
    out, _ = capsys.readouterr()
    assert out == f"{card.back}\n", "Should show back text after flipping."


def test_flip_back_to_front(
    study_session: StudySessionController, card: Card, capsys: pytest.CaptureFixture
) -> None:
    study_session.flip_card()
    assert not study_session.is_front()
    study_session.flip_card()
    assert study_session.is_front()
    card.view_side(study_session.is_front())
    out, _ = capsys.readouterr()
    assert out == f"{card.front}\n", "Should show back text after flipping."
