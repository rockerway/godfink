import configparser
from request import *
from screen import ScreenID
from screen import Screen
from characters.character import Character
from mapObjects.mapObjects import MapObjects

config = configparser.ConfigParser()
config.read('config.ini')

def login(name):
    player = readPlayer(name)
    if player == None:
        player = createPlayer(name)
    return player

def levelUP(player, space, screenID):
    player.levelUP(space)
    playerInfo = updateCharacter(player, screenID)
    return playerInfo

def transferScreen(character, screenID, x, y):
    character.x = x
    character.y = y
    characterInfo = updateCharacter(character, screenID)
    return characterInfo

def getScreen(screenID):
    screen = readScreen(screenID.value)
    return Screen(
        screen.name, 
        screen.backgroundName, 
        normalizeCharacters(screen.characters), 
        normalizeMapObjects(screen.mapObjects))

def getCharacters(screenID):
    # get all characters information that include name, role, imageName, level
    characterInfos = readCharacters()
    characters = normalizeCharacters(characterInfos)

    # Climu not in meeting room
    if screenID == ScreenID.MEETING_ROOM:
        del characters[2]

    # set character position that be got from config file
    for character in characters:
        character.x = int(config['screen' + screenID.value][character.name.lower() + '_x'])
        character.y = int(config['screen' + screenID.value][character.name.lower() + '_y'])
    
    return characters
    
def normalizeCharacters(characterInfos):
    characters = []

    for characterInfo in characterInfos:
        characters.append(Character(characterInfo))
    
    return characters

def normalizeMapObjects(mapObjectInfos):
    mapObjects = MapObjects()

    for mapObjectInfo in mapObjectInfos:
        mapObjects.add(mapObjectInfo)

    return mapObjects
