from mapObjects.mapObject import MapObject
from mapObjects.hideable import Hideable
from enum import Enum


class RadioType(Enum):
    CHAT = 1
    GO = 2
    PYTHON = 3


class Radio(MapObject, Hideable):
    def __init__(self, radio):
        self.text = radio.text
        self.var = radio.var
        self.value = radio.value
        super().__init__(
            radio.xRatio,
            radio.yRatio
        )
