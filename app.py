import tkinter
import configparser
from canvas import Canvas
from characters.character import Character
from characters.player import Player
from entities.characterInfo import CharacterInfo
from screen import *
from handler import getScreen
from handler import getCharacters

# init config
config = configparser.ConfigParser()
config.read('config.ini')

# get the game player move speed in config file
moveSpeed = int(config['game']['move_speed'])

class Application(tkinter.Frame):
    def __init__(self, master):
        self.width = int(config['window']['width'])
        self.height = int(config['window']['height'])
        self.fps = int(config['frame']['fps'])
        self.currentScreenID = ScreenID.START
        self.canControl = False
        
        super().__init__(master=master, width=self.width, height=self.height)
        self.bind("<Key>", self.key) # listen keyborad
        self.pack()
        self.canvas = Canvas(self, self.width, self.height) # create a canvas to draw all item
        self.startPage()
        self.focus_set() # focus on this frame
        self.run() # this function handler all game event logic
        self.mainloop()

    def startPage(self):
        self.player = Player(
            x = int(self.width/2), 
            y = int(self.height*2/3)
        )
        self.loadScreen() # init the screen
        self.drawScreen() # draw screen background, characters, items on canvas

    # load screen information by self.currentScreenID.
    # screen Start, MeetingRoom, WorkRoom1, WorkRoom2 have characters information
    # screen WorkRoom1, WorkRoom2 information include characters information
    # screen Start, MeetingRoom need inject characters information
    def loadScreen(self):
        # get current screen (only work_room_1 and work_room_2 can get characters)
        screen = getScreen(self.currentScreenID)
        # get characters information in screen start and screen meeting room
        if self.currentScreenID == ScreenID.START or self.currentScreenID == ScreenID.MEETING_ROOM:
            screen['characters'] = getCharacters(self.currentScreenID)
        # normalize characters information
        characters = [self.player]
        for character in screen['characters']:
            characterInfo = CharacterInfo()
            characterInfo.name = character['name']
            characterInfo.role = character['role']
            characterInfo.imageName = character['imageName']
            characterInfo.level = character['level']
            characterInfo.x = int(character['x'])
            characterInfo.y = int(character['y'])
            characters.append(Character(characterInfo))
        # normalize characters formation
        items = []
        for item in screen['items']:
            pass
        
        self.screen = Screen(
            screen['name'], 
            screen['backgroundName'], 
            characters, 
            items
        )

    def drawScreen(self):
        self.canvas.reset()
        self.canvas.setBackground(self.screen.background)
        for character in self.screen.characters:
            self.canvas.drawCharacter(character)

    # game logic
    def run(self):
        self.after(int(1000/self.fps), self.run)

    # keyboard handler
    def key(self, event):
        # print("pressed", repr(event.char))
        if not self.canControl:
            return

        key = event.char
        dx = 0
        dy = 0
        if key == 'w':
            dy = -moveSpeed
        elif key == 's':
            dy = moveSpeed
        elif key == 'a':
            dx = -moveSpeed
        elif key == 'd':
            dx = moveSpeed
        elif key == 'b':
            self.player.transfer(self.canvas)
        # update player position and feedback update state
        moveX, moveY = self.player.move(dx, dy, self.width, self.height)
        if not moveX:
            dx = 0
        if not moveY:
            dy = 0
        #move player
        self.canvas.move(self.player.canvas, dx, dy)
        # '\r'      entry
        # ' '       space
        # '\x1b'    esc
        # '\uf700'  up
        # '\uf701'  down
        # '\uf702'  left
        # '\uf703'  right
