from characters import role

class Player(role.Role):
    def __init__(self, imageName, name=None, x=0, y=0, level='1'):
        super().__init__(name, imageName, level, x=x, y=y)

    def transfer(self, canvas):
        canvas.delete(self.canvas)

    def levelUP(self, space):
        slef.level += space

    def move(self, dx, dy, width, height):
        moveX = True
        moveY = True
        self.x += dx
        self.y += dy
        if self.x > width or self.x < 0:
            self.x -= dx
            moveX = False
        if self.y > height or self.y < 0:
            self.y -= dy
            moveY = False

        return (moveX, moveY)
