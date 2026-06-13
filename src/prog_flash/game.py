# Copyright (C) 2026 K Law All rights reserved.
# Licensed under the GPLv3.

from enum import Enum, auto


class ScreenState(Enum):
    INITIAL_SCREEN = auto()
    CARD_DISPLAY = auto()


class GameLogicController:
    def __init__(self) -> None:
        self.screen_state: ScreenState = ScreenState.INITIAL_SCREEN
        self.disp_front: bool = True
        self.currentIndex: int = 0

    def flip_card(self):
        self.disp_front = not self.disp_front

    def is_front(self) -> bool:
        return self.disp_front
