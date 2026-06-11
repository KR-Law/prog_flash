# Copyright (C) 2026 K Law All rights reserved.
# Copyright (c) 2026 Your Name/Organization. All rights reserved.
# Licensed under the GPLv3.

from typing import TypedDict

import pytest
from prog_flash.card import Card
from datetime import datetime, timezone


class CardDBRow(TypedDict):
    front: str
    back: str
    updated_at: datetime


@pytest.fixture
def card() -> Card:
    db_row: CardDBRow = {
        "front": "What is Python?",
        "back": "A programming language.",
        "updated_at": datetime(2026, 6, 9, 12, 0, 0, tzinfo=timezone.utc),
    }
    card = Card(**db_row)
    return card


def test_card_initialization(card: Card) -> None:
    assert card.front == "What is Python?"
    assert card.back == "A programming language."


def test_view_card(
    card: Card, capsys: pytest.CaptureFixture, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("builtins.input", lambda: None)

    card.dsp_side = "front"
    card.view_card()
    out, _ = capsys.readouterr()
    assert out == f"{card.front}\n", "Should show front text on initial view."

    card.flip_card()
    assert card.dsp_side == "back"

    card.view_card()
    out, _ = capsys.readouterr()
    assert out == f"{card.back}\n", "Should show back text after flipping."


def test_flip_card(card: Card) -> None:
    side = card.dsp_side
    print(side)
    card.flip_card()
    assert card.dsp_side == "back"


def test_mark(card: Card) -> None:
    card.mark_card()
    assert card.marked

    card.mark_card()
    assert not card.marked
