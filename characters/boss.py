from characters.character import Character

class Boss(Character):
    def __init__(self, character):
        super().__init__(
            character['name'],
            character['imageName'],
            character['level'],
            character['x'],
            character['y']
        )