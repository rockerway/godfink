from mapObjects.mapObject import MapObject
from mapObjects.mapObjectType import MapObjectType

class Text(MapObject):
    def __init__(self, text):
        self.width = text.width
        self.height = text.height
        super().__init__(MapObjectType.TEXT, text.xRatio, text.yRatio)
