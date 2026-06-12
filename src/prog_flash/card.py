# Copyright (C) 2026 K Law All rights reserved.
# Licensed under the GPLv3.


from datetime import datetime, timezone


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

    def view_card(self, is_front) -> None:
        print(self.front) if is_front else print(self.back)

    def mark_card(self) -> None:
        self.marked = not self.marked
        self._touch()

    def update_card(self, front: str, back: str) -> None:
        self.front = front
        self.back = back
        self._touch()
