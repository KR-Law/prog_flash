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


def test_view_side(
    card: Card,
) -> None:
    result = card.view_side(is_front=True)
    assert result == card.front, "Should show front text on initial view."


def test_view_flipped_card(
    card: Card,
) -> None:
    result = card.view_side(is_front=False)
    assert result == card.back, "Should show back text."


def test_mark(card: Card) -> None:
    card.mark_card()
    assert card.marked

    card.mark_card()
    assert not card.marked


def test_update_front(card: Card) -> None:
    update_text = "Update Text for front"
    card.update_card(is_front=True, update_string=update_text)
    result: str | None = card.view_side(is_front=True)
    assert card.front == result
    assert card.back != result


def test_update_back(card: Card) -> None:
    update_text = "Update Text for back"
    card.update_card(is_front=False, update_string=update_text)
    result: str | None = card.view_side(is_front=False)
    assert card.back == result
    assert card.front != result
