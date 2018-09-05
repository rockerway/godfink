import tkinter
from enum import Enum
 
class ScreenID(Enum):
    START = '1'
    HOME = '2'
    MAP = '3'
    MEETING_ROOM = '4'
    WORK_ROOM_1 = '5'
    WORK_ROOM_2 = '6'

class Screen:
    def __init__(self, name, backgroundName, characters, mapObjects):
        self.name = name
        self.background = tkinter.PhotoImage(file='resources/backgrounds/' + backgroundName + '.gif')
        self.characters = characters
        self.mapObjects = mapObjects
