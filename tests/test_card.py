# Copyright (C) 2026 K Law All rights reserved.
# Licensed under the GPLv3.

from typing import TypedDict

import pytest
from prog_flash.card import Card


class CardDBRow(TypedDict):
    front: str
    back: str


def test_card_initialization(card: Card) -> None:
    assert card.front == "What is Python?"
    assert card.back == "A programming language."


def test_view_card(
    card: Card,
    capsys: pytest.CaptureFixture,
) -> None:
    card.view_card(is_front=True)
    out, _ = capsys.readouterr()
    assert out == f"{card.front}\n", "Should show front text on initial view."


def test_view_flipped_card(
    card: Card,
    capsys: pytest.CaptureFixture,
) -> None:
    # Simulating flipped state as back
    card.view_card(is_front=False)
    out, _ = capsys.readouterr()
    assert out == f"{card.back}\n", "Should show front text on initial view."


def test_mark(card: Card) -> None:
    card.mark_card()
    assert card.marked

    card.mark_card()
    assert not card.marked
