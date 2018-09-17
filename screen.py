import tkinter
from enum import Enum


class ScreenID(Enum):
    START = '1'
    HOME = '2'
    MAP = '3'
    MEETING_ROOM = '4'
    WORK_ROOM_1 = '5'
    WORK_ROOM_2 = '6'

    @staticmethod
    def getScreenID(screenID):
        if screenID == '1':
            return ScreenID.START
        if screenID == '2':
            return ScreenID.HOME
        if screenID == '3':
            return ScreenID.MAP
        if screenID == '4':
            return ScreenID.MEETING_ROOM
        if screenID == '5':
            return ScreenID.WORK_ROOM_1
        if screenID == '6':
            return ScreenID.WORK_ROOM_2
        return None


class Screen:
    def __init__(self, name, backgroundName, characters, mapObjects):
        self.name = name
        self.background = tkinter.PhotoImage(
            file='resources/backgrounds/' + backgroundName + '.gif')
        self.characters = characters
        self.mapObjects = mapObjects
