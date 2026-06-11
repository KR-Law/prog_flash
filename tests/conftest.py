# Copyright (C) 2026 K Law All rights reserved.
# Shared Pytest Fixtures for prog_flash tests.

from typing import TypedDict
import pytest
from prog_flash.card import Card
from prog_flash.game import StudySessionController


class CardDBRow(TypedDict):
    front: str
    back: str


@pytest.fixture(scope="module") # Changed scope for efficiency/consistency
def card() -> Card:
    """A standardized fixture providing a default, marked-up test card."""
    db_row: CardDBRow = {
        "front": "What is Python?",
        "back": "A programming language.",
    }
    retrieved_card = Card(**db_row)
    return retrieved_card


@pytest.fixture(scope="module")
def study_session() -> StudySessionController:
    """A standard fixture providing a fresh session controller instance."""
    return StudySessionController()