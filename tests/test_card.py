# Copyright (C) 2026 K Law All rights reserved.
# Copyright (c) 2026 Your Name/Organization. All rights reserved.
# Licensed under the GPLv3.

from typing import TypedDict

import pytest
from prog_flash.card import Card
from prog_flash.game import StudySessionController


class CardDBRow(TypedDict):
    front: str
    back: str


@pytest.fixture
def card() -> Card:
    db_row: CardDBRow = {
        "front": "What is Python?",
        "back": "A programming language.",
    }
    retrieved_card = Card(**db_row)
    return retrieved_card


@pytest.fixture
def study_session() -> StudySessionController:
    return StudySessionController()


def test_card_initialization(card: Card) -> None:
    assert card.front == "What is Python?"
    assert card.back == "A programming language."


def test_view_card(
    card: Card,
    study_session: StudySessionController,
    capsys: pytest.CaptureFixture,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("builtins.input", lambda: None)

    card.view_card(study_session.is_front())
    out, _ = capsys.readouterr()
    assert out == f"{card.front}\n", "Should show front text on initial view."

    study_session.flip_card()
    card.view_card(study_session.is_front())
    out, _ = capsys.readouterr()
    assert out == f"{card.back}\n", "Should show back text after flipping."


def test_mark(card: Card) -> None:
    card.mark_card()
    assert card.marked

    card.mark_card()
    assert not card.marked
