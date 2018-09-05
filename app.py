import tkinter
import configparser
from canvas import Canvas
from characters.character import Character
from characters.player import Player
from entities.characterInfo import CharacterInfo
from entities.displacement import Displacement
from entities.textInfo import TextInfo
from entities.imageInfo import ImageInfo
from mapObjects.mapObjectType import MapObjectType
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
        self.drawScreen() # draw screen background, characters, mapObjects on canvas

    # load screen information by self.currentScreenID.
    # screen Start, MeetingRoom, WorkRoom1, WorkRoom2 have characters information
    # screen WorkRoom1, WorkRoom2 information include characters information
    # screen Start, MeetingRoom need inject characters information
    def loadScreen(self):
        # get current screen (only work_room_1 and work_room_2 can get characters)
        self.screen = getScreen(self.currentScreenID)
        
        # get characters information in screen start and screen meeting room
        if self.currentScreenID == ScreenID.START or self.currentScreenID == ScreenID.MEETING_ROOM:
            self.screen.characters = getCharacters(self.currentScreenID)
        self.screen.characters.append(self.player)

    def drawScreen(self):
        self.canvas.reset()
        self.canvas.setBackground(self.screen.background)
        self.canvas.drawText(TextInfo(
            0,
            0,
            self.screen.name))
    
        for character in self.screen.characters:
            self.canvas.drawCharacter(character)
        for item in self.screen.mapObjects.items:
            self.canvas.drawImage(ImageInfo(
                int(self.width * item.xRatio),
                int(self.height * item.yRatio),
                item.image))
        for button in self.screen.mapObjects.buttons:
            self.canvas.drawButton(button)
        for listbox in self.screen.mapObjects.listboxes:
            self.canvas.drawListbox(listbox)
        for text in self.screen.mapObjects.texts:
            self.canvas.drawInput(text)

    # game logic
    def run(self):
        displacement = self.player.getDisplacement()
        for canvas in self.player.canvases:
            self.canvas.move(
                canvas,
                displacement.dx,
                displacement.dy
            )
        self.after(int(1000 / self.fps), self.run)

    def showChatBlock(self):
        if not self.canControl:
            return

    # keyboard handler (want to use some pattern to optimize)
    def key(self, event):
        # print("pressed", repr(event.char))
        if not self.canControl:
            return

        displacement = Displacement()
        key = event.char
        if key == 'w':
            displacement.dy = -moveSpeed
        elif key == 's':
            displacement.dy = moveSpeed
        elif key == 'a':
            displacement.dx = -moveSpeed
        elif key == 'd':
            displacement.dx = moveSpeed
        elif key == 'b':
            self.player.transfer(self.canvas)
        # update player position and feedback update state
        self.player.move(displacement, self.width, self.height)
        
        # '\r'      entry
        # ' '       space
        # '\x1b'    esc
        # '\uf700'  up
        # '\uf701'  down
        # '\uf702'  left
        # '\uf703'  right
