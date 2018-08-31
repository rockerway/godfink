import tkinter
from entities.displacement import Displacement

class Character:
    def __init__(self, characterInfo):
        self.canvases = []
        self.effect = None
        self.name = characterInfo.name
        self.role = characterInfo.role
        self.image = tkinter.PhotoImage(file='resources/roles/' + characterInfo.imageName + '.gif')
        self.level = characterInfo.level
        self.x = characterInfo.x
        self.y = characterInfo.y
        self.displacement = Displacement()

    def transfer(self, canvas):
        for canvas in self.canvases:
            canvas.delete(self.canvas)

    def transferEnd(self, callback):
        callback()

    def move(self, displacement, width, height):
        self.displacement.dx += displacement.dx
        self.displacement.dy += displacement.dy
        self.x += dx
        self.y += dy
        if self.x > width or self.x < 0:
            self.x -= dx
            self.displacement.dx -= displacement.dx
        if self.y > height or self.y < 0:
            self.y -= dy
            self.displacement.dy -= displacement.dy
