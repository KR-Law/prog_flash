# Copyright (C) 2026 K Law All rights reserved.
# Licensed under the GPLv3.


from datetime import datetime, timezone


class Card:
    def __init__(self, front: str, back: str) -> None:
        self.front: str = front
        self.back: str = back
        self.marked: bool = False
        self.number_correct: int = 0
        self.created_at: datetime = datetime.now(timezone.utc)
        self.updated_at: datetime = self.created_at
        self.viewed_at: datetime = self.created_at

    def _touch(self) -> None:
        self.updated_at = datetime.now(timezone.utc)

    def get_side(self, is_front) -> str | None:
        """Get text for side to view"""
        if is_front:
            return self.front
        else:
            return self.back

    def get_num_correct(self) -> int:
        return self.number_correct
    
    def mark_correct(self) -> None:
        """Mark card as correct"""
        self.marked = not self.marked
        self.number_correct += 1
        self._touch()

    def update_card(self, is_front: bool, update_string: str) -> None:
        """Update card depending on value of is_front if true update front else update back"""
        if is_front:
            self.front = update_string
        else:
            self.back = update_string
        self._touch()
