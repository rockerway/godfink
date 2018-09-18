import tkinter
import os
from mapObjects.button import Button
from mapObjects.text import Text
from mapObjects.radio import Radio
from mapObjects.radio import RadioType
from entities.buttonInfo import ButtonInfo
from entities.inputInfo import InputInfo
from entities.radioInfo import RadioInfo
from fs.file import File
from fs.file import ModeType


class ChatUI:
    def __init__(self, root):
        self.root = root
        self.canExit = True
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
        self.codeResult = ""

    def key(self, event):
        key = event.char
        if key == '\x1b':
            self.hide()

    def hide(self):
        if not self.canExit:
            return
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

        if chatType == RadioType.CHAT.value:
            self.input.canvas.delete(0.0, message.__len__() - 1.0)
            message = 'Me: %s' % message.replace('\n', '\n        ')[:-8]
            self.writeMessage(message)
        if chatType == RadioType.GO.value:
            self.runCode('input.go', message)
        if chatType == RadioType.PYTHON.value:
            self.runCode('input.py', message)

    def writeMessage(self, message):
        self.output.canvas.config(state=tkinter.NORMAL)
        self.output.canvas.insert(tkinter.INSERT, '%s' % message)
        self.output.canvas.config(state=tkinter.DISABLED)

    def runCode(self, inputName, code, ):
        File.write("jail/std/" + inputName, code)
        scriptFileName = ""
        if inputName == "input.py":
            scriptFileName = "python"
        elif inputName == "input.go":
            scriptFileName = "go"
        os.system("sh ${PWD}/jail/%s" % scriptFileName)
        output = File.read("jail/std/output")
        error = File.read("jail/std/error")
        if output != "" and error == "":
            self.canExit = True
            self.writeMessage("---------- OUTPUT ----------\n")
            self.writeMessage(output)
            self.writeMessage("------------------------------\n")
            self.codeResult = output
        if error != "":
            self.writeMessage("---------- ERROR -----------\n")
            self.writeMessage(error)
            self.writeMessage("------------------------------\n")
