import requests
import json
from collections import namedtuple
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
ENDPOINT_URL = "http://" + config['database']['url'] + "/graphql"
width = int(config['window']['width'])
height = int(config['window']['height'])


def request(query, variables='{}'):
    response = requests.post(
        ENDPOINT_URL, json={'query': query, 'variables': variables})
    # return json.loads(response.text)
    return json.loads(
        response.text,
        object_hook=lambda d: namedtuple('Obj', d.keys())(*d.values())
    )


def readPlayer(name):
    query = """query GetPlayer($name: String!) {
      player(name: $name) {
        id
        name
        role
        screenID
        imageName
        level
        xRatio
        yRatio
      }
    }"""
    variables = {'name': name}
    result = request(query, variables)
    if len(result.data.player) == 0:
        return None
    else:
        return result.data.player[0]


def createPlayer(name):
    query = """mutation CreateCharacter($input: CreateCharacterInput!) {
      createCharacter(input: $input) {
        id
        screenID
        name
        role
        imageName
        level
        xRatio
        yRatio
      }
    }"""
    variables = {
        'input': {
            'screenID': '2',
            'name': name,
            'role': 'player',
            'imageName': 'player',
            'level': '1',
            'xRatio': 0.5,
            'yRatio': 0.5
        }
    }
    result = request(query, variables)
    return result.data.createCharacter


def updateCharacter(character, screenID):
    query = """mutation UpdateCharacter($input: UpdateCharacterInput!) {
      updateCharacter(input: $input) {
        id
        screenID
        name
        role
        imageName
        level
        xRatio
        yRatio
      }
    }"""
    variables = {
        'input': {
            'id': character.id,
            'screenID': screenID,
            'name': character.name,
            'role': character.role,
            'imageName': character.imageName,
            'level': character.level,
            'xRatio': character.x / width,
            'yRatio': character.y / height
        }
    }
    result = request(query, variables)
    return result.data.updateCharacter


def readScreen(screenID):
    query = """query GetScene($id: ID!) {
      screen(id: $id) {
        name
        backgroundName
        characters {
          id
          name
          role
          imageName
          level
          xRatio
          yRatio
        }
        mapObjects {
          id
          screenID
          imageName
          name
          action
          targetScreenID
          xRatio
          yRatio
        }
      }
    }"""
    variables = {
        'id': screenID
    }
    result = request(query, variables)
    return result.data.screen


def readCharacters():
    query = """{
      characters {
        id
        name
        role
        imageName
        level
        xRatio
        yRatio
      }
    }"""
    result = request(query)
    return result.data.characters
