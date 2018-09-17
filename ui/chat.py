import tkinter
from mapObjects.button import Button
from mapObjects.text import Text
from mapObjects.radio import Radio
from mapObjects.radio import RadioType
from entities.buttonInfo import ButtonInfo
from entities.inputInfo import InputInfo
from entities.radioInfo import RadioInfo


class ChatUI:
    def __init__(self, root):
        self.root = root
        self.chatType = tkinter.IntVar(value=RadioType.CHAT.value)
        self.output = Text(InputInfo(0, 0.1, 50, 17, withScrollBar=True))
        self.input = Text(
            InputInfo(0, 0.6, 50, 12, callback=self.key, withScrollBar=True))
        self.exitButton = Button(ButtonInfo(0.1, 0.95, "Close", self.hide))
        self.sendButton = Button(ButtonInfo(0.3, 0.95, "Send", self.send))
        self.radios = [
            Radio(RadioInfo(0.1, 0.05, "Chat", self.chatType, RadioType.CHAT.value)),
            Radio(RadioInfo(0.2, 0.05, "Go", self.chatType, RadioType.GO.value)),
            Radio(RadioInfo(0.3, 0.05, "Python",
                            self.chatType, RadioType.PYTHON.value))
        ]

    def key(self, event):
        key = event.char
        if key == '\x1b':
            self.hide()

    def hide(self):
        self.output.hide()
        self.input.hide()
        self.exitButton.hide()
        self.sendButton.hide()
        for radio in self.radios:
            radio.hide()
        self.root.focus_set()

    def show(self):
        self.output.show()
        self.input.show()
        self.exitButton.show()
        self.sendButton.show()
        for radio in self.radios:
            radio.show()
        self.input.canvas.focus_set()

    def send(self):
        chatType = self.chatType.get()
        message = self.input.canvas.get('1.0', tkinter.END)
        self.input.canvas.delete(0.0, message.__len__() - 1.0)

        if chatType == RadioType.CHAT.value:
            message = 'Me: %s' % message.replace('\n', '\n        ')[:-8]
            self.output.canvas.config(state=tkinter.NORMAL)
            self.output.canvas.insert(tkinter.INSERT, '%s' % message)
            self.output.canvas.config(state=tkinter.DISABLED)
        if chatType == RadioType.GO.value:
            pass
        if chatType == RadioType.PYTHON.value:
            pass
