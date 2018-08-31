from characters.character import Character
from entities.characterInfo import CharacterInfo

class Player(Character):
    def __init__(self, name=None, x=0, y=0, level='1'):
        characterInfo = CharacterInfo()
        characterInfo.name = name
        characterInfo.role = 'player'
        characterInfo.imageName = 'player'
        characterInfo.level = level
        characterInfo.x = x
        characterInfo.y = y
        super().__init__(characterInfo)

    def transfer(self, canvas):
        for obj in self.canvases:
            canvas.delete(obj)

    def levelUP(self, space):
        slef.level += space
