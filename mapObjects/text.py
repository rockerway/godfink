from mapObjects.mapObject import MapObject
from mapObjects.hideable import Hideable


class Text(MapObject, Hideable):
    def __init__(self, text):
        self.frame = None
        self.width = text.width
        self.height = text.height
        self.command = text.callback
        self.withScrollBar = text.withScrollBar
        if self.withScrollBar:
            self.scrollBar = None
        super().__init__(text.xRatio, text.yRatio)
