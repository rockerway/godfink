import tkinter

class Role:
    def __init__(self, name, imageName, level, x=0, y=0):
        self.canvas = None
        self.image = tkinter.PhotoImage(file='resources/roles/' + imageName + '.gif')
        self.name = name
        self.level = level
        self.x = x
        self.y = y

    def transfer(self, canvas):
        canvas.delete(self.canvas)

    def transferEnd(self, callback):
        callback()
