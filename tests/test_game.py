# Copyright (C) 2026 K Law All rights reserved.
# Licensed under the GPLv3.

from prog_flash.card import Card
from prog_flash.game import GameLogicController


def test_flip_back_front_to_back(
    study_session: GameLogicController,
    card: Card,
) -> None:
    assert study_session.is_front()
    study_session.flip_card()
    assert not study_session.is_front()
    result: str = card.get_side(study_session.is_front())
    assert result == f'{card.back}'


def test_flip_back_to_front(study_session: GameLogicController, card: Card) -> None:
    study_session.flip_card()
    assert not study_session.is_front()
    study_session.flip_card()
    assert study_session.is_front()
    result: str = card.get_side(study_session.is_front())
    assert result == f'{card.front}', 'Should show front text after flipping.'
