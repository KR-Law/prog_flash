# Copyright (C) 2026 K Law All rights reserved.
# Licensed under the GPLv3.


from datetime import datetime, timezone
import string


class Card:
    def __init__(self, front: str, back: str) -> None:
        self.front: str = front
        self.back: str = back
        self.marked: bool = False
        self.correct_count: int = 0
        self.created_at: datetime = datetime.now(timezone.utc)
        self.updated_at: datetime = self.created_at
        self.viewed_at: datetime = self.created_at

    def _touch(self) -> None:
        """Update the last modified timestamp"""
        self.updated_at = datetime.now(timezone.utc)

    def get_side(self, is_front: bool) -> str:
        """Get text for side to view (front or back)"""
        if is_front:
            return self.front
        else:
            return self.back

    @property
    def count(self) -> int:
        """Return the number of correct marks"""
        return self.correct_count

    def mark_correct(self) -> None:
        """Mark card as correct (toggles marked status, increments counter)"""
        self.marked = True
        self.correct_count += 1
        self._touch()

    def reset_marked(self) -> None:
        """Reset Marked to a unmarked status"""
        if self.marked:
            self.marked = False

    def update_card(self, is_front: bool, new_content: str) -> None:
        """Update card content depending on value of is_front (front or back)"""
        if not new_content or not isinstance(new_content, str):
            raise TypeError('No update string passed')
        if is_front:
            self.front = new_content
        else:
            self.back = new_content
        self._touch()
