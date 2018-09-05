from mapObjects.mapObjectType import MapObjectType
from mapObjects.button import Button
from mapObjects.listbox import Listbox
from mapObjects.text import Text
from mapObjects.item import Item

class MapObjects:
    def __init__(self):
        self.buttons = []
        self.listboxes = []
        self.texts = []
        self.items = []

    def add(self, mapObjectInfo):
        if mapObjectInfo.type == MapObjectType.BUTTON.value:
            self.buttons.append(Button(mapObjectInfo))
        if mapObjectInfo.type == MapObjectType.LISTBOX.value:
            self.listboxes.append(Listbox(mapObjectInfo))
        if mapObjectInfo.type == MapObjectType.TEXT.value:
            self.texts.append(Text(mapObjectInfo))
        if mapObjectInfo.type == MapObjectType.ITEM.value:
            self.items.append(Item(mapObjectInfo))