from characters import role

class NPC(role.Role):
    def __init__(self, imageName, name, x=0, y=0, level="200 Plus"):
        super().__init__(name, imageName, level, x=x, y=y)