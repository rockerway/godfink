import configparser
from request import *
from screen import ScreenID
from screen import Screen
from characters.character import Character
from mapObjects.item import Item
from actions.event import Event

config = configparser.ConfigParser()
config.read('config.ini')
width = int(config['window']['width'])
height = int(config['window']['height'])


def login(name):
    player = readPlayer(name)
    if player == None:
        player = createPlayer(name)
    return player


def levelUP(player, space, screenID):
    player.levelUP(space)
    playerInfo = updateCharacter(player, screenID.value)
    return playerInfo


def characterTransferScreen(character, screenID):
    characterInfo = updateCharacter(character, screenID.value)


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
        character.x = float(config['screen' + screenID.value]
                            [character.name.lower() + '_xRatio']) * width
        character.y = float(config['screen' + screenID.value]
                            [character.name.lower() + '_yRatio']) * height

    return characters


def normalizeCharacters(characterInfos):
    characters = []

    for characterInfo in characterInfos:
        character = Character(characterInfo)
        normalizeEvents(character.events, characterInfo.events)
        characters.append(character)

    return characters


def normalizeEvents(characterEvents, eventInfos):
    for eventInfo in eventInfos:
        characterEvents.append(Event(eventInfo))


def normalizeMapObjects(mapObjectInfos):
    mapObjects = []

    for mapObjectInfo in mapObjectInfos:
        mapObjects.append(Item(mapObjectInfo))

    return mapObjects
