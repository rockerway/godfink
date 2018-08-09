from characters import role

class NPC(role.Role):
    def __init__(self, imageName, name=None, x=0, y=0, level="200 Plus"):
        super().__init__(imageName, name=name, x=x, y=y, level=level)