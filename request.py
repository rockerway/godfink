import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
ENDPOINT_URL = "http://" + config['database']['url'] + "/graphql"

def request(query, variables='{}'):
    response = requests.post(ENDPOINT_URL, json={'query': query, 'variables': variables})
    return json.loads(response.text)

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
    players = request(query, variables)
    if len(players['data']['player']) == 0:
        return None
    else:
        return players['data']['player'][0]

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
    player = request(query, variables)
    return player['data']['character']

def updateCharacter(character):
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
            'screenID': character.screenID,
            'name': character.name,
            'role': character.role,
            'imageName': character.imageName,
            'level': character.level,
            'x': character.x,
            'y': character.y
        }
    }
    character = request(query, variables)
    return character['data']['character']

def readScreen(screenID):
    query = """query GetScreen($id: ID!) {
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
          items {
          image
          width
          height
          x
          y
        }
      }
    }"""
    variables = {
        'id': screenID
    }
    screen = request(query, variables)
    return screen['data']['screen']

def readCharacters():
    query = """{
      characters {
        name
        role
        imageName
        level
      }
    }"""
    characters = request(query)
    return characters['data']['characters']
