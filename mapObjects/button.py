from mapObjects.mapObject import MapObject
from mapObjects.mapObjectType import MapObjectType

class Button(MapObject):
    def __init__(self, button):
        self.text = button.text
        self.command = button.callback
        super().__init__(
            MapObjectType.BUTTON, 
            button.xRatio, 
            button.yRatio
        )
