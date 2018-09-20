import tkinter
import configparser
import math
from canvas import Canvas
from characters.character import Character
from characters.player import Player
from entities.characterInfo import CharacterInfo
from entities.displacement import Displacement
from entities.textInfo import TextInfo
from entities.imageInfo import ImageInfo
from screen import *
from ui.startPage import StartPageUI
from ui.chat import ChatUI
from handler import getScreen
from handler import getCharacters
from handler import characterTransferScreen
from handler import levelUP

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
        self.beforeScreenID = None
        self.canControl = False
        self.chatUI = None
        self.actions = {}
        self.shot1Image = tkinter.PhotoImage(
            file='resources/shots/explosive.gif')
        self.shot2Image = tkinter.PhotoImage(
            file='resources/shots/fish.gif')
        self.shot1ID = None
        self.shot2ID = None
        self.help = False

        super().__init__(master=master, width=self.width, height=self.height)
        self.bind("<Key>", self.key)  # listen keyborad
        self.pack()
        # create a canvas to draw all item
        self.canvas = Canvas(self, self.width, self.height)
        self.startPage()
        self.focus_set()  # focus on this frame
        self.run()  # this function handler all game event logic
        self.mainloop()

    def startPage(self):
        self.actions['changeScreen'] = self.changeScreen
        self.actions['dream'] = self.dream
        self.actions['communicate'] = self.communicate
        self.player = Player(
            xRatio=0.5,
            yRatio=2/3
        )

        self.loadScreen()  # init the screen
        self.drawScreen()  # draw screen background, characters, mapObjects on canvas
        self.drawStartPageUI()

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

    def drawScreen(self):
        self.canvas.reset()
        self.canvas.setBackground(self.screen.background)
        self.canvas.drawText(
            TextInfo(
                10,
                10,
                self.screen.name),
            startFrom=tkinter.NW
        )

        for character in self.screen.characters:
            self.canvas.drawCharacter(character)
        for mapObject in self.screen.mapObjects:
            self.canvas.drawImage(ImageInfo(
                int(self.width * mapObject.xRatio),
                int(self.height * mapObject.yRatio),
                mapObject.image))
        self.canvas.drawCharacter(self.player)
        self.drawChatBlock()

    # game logic
    def run(self):
        # login and success get player information from DB
        if self.startPageUI.player:
            # initial player
            self.player = Player(
                self.startPageUI.player.name,
                self.startPageUI.player.xRatio,
                self.startPageUI.player.yRatio,
                self.startPageUI.player.level,
                self.startPageUI.player.id)
            # set current screen ID that player in
            self.currentScreenID = ScreenID.getScreenID(
                self.startPageUI.player.screenID)
            self.startPageUI.player = None

            self.loadScreen()
            self.drawScreen()
            self.canControl = True
            self.focus_set()

        if self.chatUI.codeResult != "" or self.chatUI.getLevel != 0:
            level = int(math.ceil(len(self.chatUI.codeResult) / 20)
                        ) + self.chatUI.getLevel
            levelUP(self.player, level, self.currentScreenID)
            for canvas in self.player.canvases:
                self.canvas.deleteWeight(canvas)
            self.player.canvases = []
            self.canvas.drawCharacter(self.player)
            self.chatUI.codeResult = ""
            self.chatUI.getLevel = 0

        displacement = self.player.getDisplacement()
        for canvas in self.player.canvases:
            self.canvas.move(
                canvas,
                displacement.dx,
                displacement.dy
            )

        for character in self.screen.characters:
            if character.role != 'boss':
                continue
            if self.getDistance(character.x, character.y) < 100:
                self.canvas.itemconfig(character.effect, state=tkinter.NORMAL)
            else:
                self.canvas.itemconfig(character.effect, state=tkinter.HIDDEN)

        if self.chatUI.help:
            playerLevel = int(self.player.level)
            message = ''
            if playerLevel >= 2:
                message += '%s :\t%s\n' % (
                    'System :',
                    '快去找 Ace 詢問 "learn", "CI/CD" 相關問題')
            if playerLevel >= 3:
                message += '%s :\t%s\n' % (
                    'System :',
                    '快去找 Angular 詢問 "Route53" 相關問題')
            if playerLevel >= 10:
                message += '%s :\t%s\n' % (
                    'System :',
                    '快去找 Chrome 詢問 "TDD" 相關問題')
            if playerLevel >= 30:
                message += '%s :\t%s\n' % (
                    'System :',
                    '快去找 JaKC 詢問 "TokenExchange", "PoP的nonce為何payload要先hash", "好多RFC要讀喔", "我以為我懂，其實我不懂，而且我不懂我哪裡不懂" 相關問題')
                message += '%s :\t%s\n' % (
                    'System :',
                    '快去找 YoSi 詢問 "LL大大說明為了code簡潔甚至有團隊限制function只能在幾行內解決" 相關問題')
                message += '%s :\t%s\n' % (
                    'System :',
                    '快去找 Climu 詢問 "Python的Address這麼不認真" 相關問題')
            if playerLevel >= 2:
                self.chatUI.writeMessage(message)
            self.chatUI.help = False

        self.after(int(1000 / self.fps), self.run)

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
        elif key == 'e':
            obj = self.getClosestObject()
            if obj:
                self.actions[obj.action](obj)
        elif key == 'm':
            self.meeting()
        elif key == '1':
            if not self.shot1ID:
                self.shot1ID = self.canvas.drawImage(
                    ImageInfo(int(0.5 * self.width), int(0.5 * self.height), self.shot1Image))
        elif key == '2':
            if not self.shot2ID:
                self.shot2ID = self.canvas.drawImage(
                    ImageInfo(int(0.5 * self.width), int(0.5 * self.height), self.shot2Image))
        elif key == '\r':
            self.chatUI.show()
        elif key == '\x1b':
            if self.shot1ID:
                self.canvas.deleteWeight(self.shot1ID)
                self.shot1ID = None
            if self.shot2ID:
                self.canvas.deleteWeight(self.shot2ID)
                self.shot2ID = None
        # elif key == 'b':
        #     self.player.transfer(self.canvas)

        # update player position
        self.player.move(displacement, self.width, self.height)

        # '\r'      entry
        # ' '       space
        # '\x1b'    esc
        # '\uf700'  up
        # '\uf701'  down
        # '\uf702'  left
        # '\uf703'  right

    def drawStartPageUI(self):
        self.startPageUI = StartPageUI()
        self.canvas.drawButton(self.startPageUI.button)
        self.canvas.drawInput(self.startPageUI.text)

    def drawChatBlock(self):
        if not self.chatUI:
            self.chatUI = ChatUI(self)
        self.canvas.drawInput(self.chatUI.output,
                              startFrom=tkinter.NW, canModify=False)
        self.canvas.drawInput(self.chatUI.input, startFrom=tkinter.NW)
        self.canvas.drawButton(self.chatUI.sendButton)
        self.canvas.drawButton(self.chatUI.clearButton)
        self.canvas.drawButton(self.chatUI.exitButton)
        for radio in self.chatUI.radios:
            self.canvas.drawRadio(radio)
        self.chatUI.hide()
        self.help = True

    def getClosestObject(self):
        closestObject = None
        minDistance = 100
        for character in self.screen.characters:
            distance = self.getDistance(character.x, character.y)
            if distance < minDistance:
                minDistance = distance
                closestObject = character

        for mapObject in self.screen.mapObjects:
            distance = self.getDistance(
                mapObject.xRatio * self.width, mapObject.yRatio * self.height)
            if distance < minDistance:
                minDistance = distance
                closestObject = mapObject

        return closestObject

    def getDistance(self, x, y):
        width = self.player.x - x
        height = self.player.y - y

        return math.sqrt(width * width + height * height)

    def changeScreen(self, mapObject):
        targetScreenID = ScreenID.getScreenID(mapObject.targetScreenID)
        if targetScreenID:
            self.beforeScreenID = self.currentScreenID
            self.currentScreenID = targetScreenID
        else:
            if self.beforeScreenID:
                self.currentScreenID = self.beforeScreenID
            else:
                self.currentScreenID = ScreenID.MAP
        self.loadScreen()
        self.setPlayerPosition()
        self.drawScreen()

    def meeting(self):
        if self.currentScreenID == ScreenID.MEETING_ROOM:
            return

        self.beforeScreenID = self.currentScreenID
        self.currentScreenID = ScreenID.MEETING_ROOM
        self.loadScreen()
        self.setPlayerPosition()
        self.drawScreen()

    def setPlayerPosition(self):
        target = 'Door'
        if self.currentScreenID == ScreenID.MAP:
            if self.beforeScreenID == ScreenID.HOME:
                target = 'Home'
            elif self.beforeScreenID == ScreenID.WORK_ROOM_1:
                target = 'Work1'
            elif self.beforeScreenID == ScreenID.WORK_ROOM_2:
                target = 'Work2'
            elif int(self.player.level) >= 100:
                target = 'Work2'
            else:
                target = 'Work1'

        for mapObject in self.screen.mapObjects:
            if mapObject.name == target:
                xRatio, yRatio = mapObject.xRatio, mapObject.yRatio
                break

        self.player.x = xRatio * self.width
        self.player.y = yRatio * self.height

        if self.currentScreenID == ScreenID.MEETING_ROOM:
            return
        characterTransferScreen(self.player, self.currentScreenID)

    def dream(self, mapObject):
        self.chatUI.canExit = False
        self.chatUI.show()

    def communicate(self, character):
        if self.currentScreenID == ScreenID.MEETING_ROOM:
            if character.id == '5':
                message = '%s :\t%s\n' % (
                    character.name,
                    '#@%&*')
                self.chatUI.writeMessage(message)
            elif character.id == '1':
                message = '%s :\t%s\n' % (
                    character.name,
                    'ABCD RFC')
                self.chatUI.writeMessage(message)
            elif character.id == '2':
                message = '%s :\t%s\n' % (
                    character.name,
                    '123 6749')
                self.chatUI.writeMessage(message)
            elif character.id == '4':
                message = '%s :\t%s\n' % (
                    character.name,
                    '...')
                self.chatUI.writeMessage(message)
            elif character.id == '7':
                message = '%s :\t%s\n' % (
                    character.name,
                    'PoP 才能保證 Auth Server 接收到的 request 是從合法的 Client 送來的，避免機敏性資料出現意外')
                self.chatUI.writeMessage(message)
            return
        self.chatUI.show(character, int(self.player.level))
