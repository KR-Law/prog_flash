# Copyright (C) 2026 K Law All rights reserved.
# Licensed under the GPLv3.


from datetime import datetime, timezone
from turtle import back


class Card:
    def __init__(self, front: str, back: str) -> None:
        self.front: str = front
        self.back: str = back
        self.marked: bool = False
        self.created_at: datetime = datetime.now(timezone.utc)
        self.updated_at: datetime = self.created_at
        self.viewed_at: datetime = self.created_at

    def _touch(self) -> None:
        self.updated_at = datetime.now(timezone.utc)

    def view_side(self, is_front) -> str | None:
        """Get text for side to view"""
        if is_front:
            return self.front
        else:
            return self.back

    def mark_card(self) -> None:
        self.marked = not self.marked
        self._touch()

    def update_card(self, is_front: bool, update_string: str) -> None:
        if is_front:
            self.front = update_string
        else:
            self.back = update_string
        self._touch()
