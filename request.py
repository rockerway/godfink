import requests
import json
from collections import namedtuple
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
ENDPOINT_URL = "http://" + config['database']['url'] + "/graphql"

def request(query, variables='{}'):
    response = requests.post(ENDPOINT_URL, json={'query': query, 'variables': variables})
    # return json.loads(response.text)
    return json.loads(
        response.text,
        object_hook=lambda d: namedtuple('Obj', d.keys())(*d.values())
    )

def readPlayer(name):
    query = """query GetPlayer($name: String!) {
      player(name: $name) {
        id
        role
        screenID
        imageName
        level
        x
        y
      }
    }"""
    variables = {'name': name}
    result = request(query, variables)
    if len(result.data) == 0:
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
        x
        y
      }
    }"""
    variables = {
        'input': {
            'screenID': 2,
            'name': name,
            'role': 'player',
            'imageName': 'player',
            'level': '1',
            'x': 0,
            'y': 0
        }
    }
    result = request(query, variables)
    return result.data.character

def updateCharacter(character, screenID):
    query = """mutation UpdateCharacter($input: UpdateCharacterInput!) {
      updateCharacter(input: $input) {
        id: ID
        screenID
        name
        role
        imageName
        level
        x
        y
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
            'x': character.x,
            'y': character.y
        }
    }
    result = request(query, variables)
    return result.data.character

def readScreen(screenID):
    query = """query GetScene($id: ID!) {
      screen(id: $id) {
        name
        backgroundName
        characters {
          name
          role
          imageName
          level
          x
          y
        }
        mapObjects {
          id
          screenID
          type
          xRatio
          yRatio
          ... on Button {
            text
            callback
          }
          ... on Text {
            width
            height
          }
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
        name
        role
        imageName
        level
        x
        y
      }
    }"""
    result = request(query)
    return result.data.characters
