from characters import role

class Boss(role.Role):
    def __init__(self, imageName, name, x=0, y=0):
        super().__init__(name, imageName, "???", x=x, y=y)