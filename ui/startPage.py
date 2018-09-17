import tkinter
from mapObjects.button import Button
from mapObjects.text import Text
from entities.buttonInfo import ButtonInfo
from entities.inputInfo import InputInfo
from handler import login

class StartPageUI:
    def __init__(self):
        self.textUseEntry = False
        self.player = None
        self.button = Button(ButtonInfo(0.5, 0.875, 'start', self.start))
        self.text = Text(InputInfo(0.5, 0.5, 20, 1, self.key))

    def start(self):
        name = self.text.canvas.get('1.0', tkinter.END)
        name = name[:-1]
        self.player = login(name)

    def key(self, event):
        key = event.char
        if key == '\r':
            self.textUseEntry = True
            self.start()