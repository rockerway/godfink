from characters.character import Character
from entities.characterInfo import CharacterInfo


class Player(Character):
    def __init__(self, name=None, xRatio=0, yRatio=0, level='1', id=None):
        characterInfo = CharacterInfo({
            'id': id,
            'name': name,
            'role': 'player',
            'imageName': 'player',
            'level': level,
            'xRatio': xRatio,
            'yRatio': yRatio
        })
        super().__init__(characterInfo)

    def transfer(self, canvas):
        for obj in self.canvases:
            canvas.delete(obj)

    def levelUP(self, space):
        self.level = str(int(self.level) + space)
