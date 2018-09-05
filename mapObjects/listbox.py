from mapObjects.mapObject import MapObject
from mapObjects.mapObjectType import MapObjectType

class Listbox(MapObject):
    def __init__(self, listbox):
        self.width = listbox['width']
        self.height = listbox['height']
        super.__init__(MapObjectType.LISTBOX, listbox['xRatio'], listbox['yRatio'])
