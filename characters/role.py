import tkinter

class Role:
    def __init__(self, imageName, name=None, x=0, y=0, level=1):
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

    def upgrade(self, space):
        slef.level += space  

    def move(dx, dy):
        self.x += dx
        self.y += dy
