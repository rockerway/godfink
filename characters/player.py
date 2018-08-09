from characters import role

class Player(role.Role):
    def __init__(self, imageName, name=None, x=0, y=0, level=1):
        super().__init__(imageName, name=name, x=x, y=y)

    def transfer(self, canvas):
        canvas.delete(self.canvas)
