import configparser
from request import *
import screen as s

config = configparser.ConfigParser()
config.read('config.ini')

def login(name):
    player = readPlayer(name)
    if player == None:
        player = createPlayer(name)
    return player

def levelUP(player, space):
    player.levelUP(space)
    playerInfo = updateCharacter(player)
    return playerInfo

def transferScreen(character, screenID, x, y):
    character.screenID = screenID
    character.x = x
    character.y = y
    characterInfo = updateCharacter(character)
    return characterInfo

def getScreen(screenID):
    return readScreen(screenID.value)

def getCharacters(screenID):
    # get all characters information that include name, role, imageName, level
    characters = readCharacters()
    # Climu not in meeting room
    if screenID == s.ScreenID.MEETING_ROOM:
        del characters[2]
    # set character position that be got from config file
    for character in characters:
        character['x'] = config['screen' + screenID.value][character['name'].lower() + '_x']
        character['y'] = config['screen' + screenID.value][character['name'].lower() + '_y']
    
    return characters
