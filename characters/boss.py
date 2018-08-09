from characters import role

class Boss(role.Role):
    def __init__(self, imageName, name=None, x=0, y=0):
        super().__init__(imageName, name=name, x=x, y=y, level="???")