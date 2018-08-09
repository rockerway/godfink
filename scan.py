import tkinter
from characters import role

class Scan:
    def __init__(self, name, width, height, backgroundName='default'):
        self.name = name
        self.width = width
        self.height = height
        self.background = tkinter.PhotoImage(file='resources/backgrounds/' + backgroundName + '.gif')
        self.items = []
