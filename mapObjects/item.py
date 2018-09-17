from tkinter import PhotoImage
from mapObjects.mapObject import MapObject


class Item(MapObject):
    def __init__(self, item):
        self.image = PhotoImage(
            file='resources/mapObjects/' + item.imageName + '.gif')
        self.targetScreenID = item.targetScreenID
        self.name = item.name
        self.action = item.action
        super().__init__(item.xRatio, item.yRatio)
