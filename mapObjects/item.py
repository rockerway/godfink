from tkinter import PhotoImage
from mapObjects.mapObject import MapObject
from mapObjects.mapObjectType import MapObjectType

class Item(MapObject):
    def __init(self, item):
        self.image = PhotoImage(file='resources/roles/' + item['imageName'] + '.gif')
        super.__init__(MapObjectType.ITEM, item['xRatio'], item['yRatio'])