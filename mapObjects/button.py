from mapObjects.mapObject import MapObject
from mapObjects.hideable import Hideable


class Button(MapObject, Hideable):
    def __init__(self, button):
        self.text = button.text
        self.command = button.callback
        super().__init__(
            button.xRatio,
            button.yRatio
        )
