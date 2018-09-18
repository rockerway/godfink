class CharacterInfo:
    def __init__(self, character):
        self.id = character['id']
        self.name = character['name']
        self.role = character['role']
        self.imageName = character['imageName']
        self.level = character['level']
        self.xRatio = character['xRatio']
        self.yRatio = character['yRatio']
        self.events = []
        self.action = ''
        self.mantra = ''
