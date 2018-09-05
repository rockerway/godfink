class CharacterInfo:
    def __init__(self, character):
        self.name = character['name']
        self.role = character['role']
        self.imageName = character['imageName']
        self.level = character['level']
        self.x = int(character['x'])
        self.y = int(character['y'])