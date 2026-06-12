# Copyright (C) 2026 K Law All rights reserved.
# Licensed under the GPLv3.


class StudySessionController:
    def __init__(self) -> None:
        self.disp_front: bool = True
        self.currentIndex: int = 0

    def flip_card(self):
        self.disp_front = not self.disp_front

    def is_front(self) -> bool:
        return self.disp_front
