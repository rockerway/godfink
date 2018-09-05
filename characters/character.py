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

    def getDisplacement(self):
        displacement = self.displacement
        self.displacement = Displacement()
        return displacement

    def transfer(self, canvas):
        for canvas in self.canvases:
            canvas.delete(self.canvas)

    def transferEnd(self, callback):
        callback()

    def move(self, displacement, width, height):
        nextX = self.x + displacement.dx
        nextY = self.y + displacement.dy

        if 0 < nextX and nextX < width:
            self.displacement.dx += displacement.dx
            self.x = nextX
        if 0 < nextY and nextY < height:
            self.displacement.dy += displacement.dy
            self.y = nextY