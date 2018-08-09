import tkinter
from canvas import Canvas
from characters import player
from characters import npc
from characters import boss
from scan import Scan

class Application(tkinter.Frame):
    def __init__(self, master, width, height, fps):
        self.width = width
        self.height = height
        self.fps = fps
        self.currentScanNum = 0

        self.initRole()
        self.initScan()
        
        super().__init__(master=master, width=self.width, height=self.height)
        self.bind("<Key>", self.key)
        self.pack()
        self.canvas = Canvas(self, self.width, self.height)

        self.canvas.setBackground(self.scans[self.currentScanNum].background)
        self.canvas.drawRole(self.player)
        self.canvas.drawRole(self.jakc)
        self.canvas.drawRole(self.yosi)
        self.canvas.drawRole(self.climu)
        self.canvas.drawRole(self.ic)
        self.canvas.drawRole(self.chrome)
        self.canvas.drawRole(self.angular)
        self.canvas.drawRole(self.hack)

        self.focus_set()
        self.run()
        self.mainloop()

    def initRole(self):
        num = 7
        space = int(self.width / (num + 1))
        self.player = player.Player("player", x=int(self.width/2), y=int(self.height/2))
        self.jakc = boss.Boss("role1", name="JaKC", x=space*1, y=200)
        self.yosi = boss.Boss("role4", name="YoSi", x=space*2, y=200)
        self.climu = boss.Boss("role5", name="Climu", x=space*3, y=200)
        self.ic = npc.NPC("role2", name="IC", x=space*4, y=200)
        self.chrome = npc.NPC("role3", name="Chrome", x=space*5, y=200)
        self.angular = npc.NPC("role6", name="Angular", x=space*6, y=200)
        self.hack = npc.NPC("role7", name="Hack", x=space*7, y=200, level="200")

    def initScan(self):
        startScan = Scan("Start", self.width, self.height)
        homeScan = Scan("Home", self.width, self.height, "home")
        mapScan = Scan("Map", self.width, self.height, "map")
        c1Scan = Scan("7樓可怕的地方", self.width, self.height)
        c2Scan = Scan("9樓一堆God的地方，可是我叫Tod >.<", self.width, self.height)
        meetingRoomScan = Scan("Meeting Room", self.width, self.height)
        self.scans = [startScan, homeScan, mapScan, c1Scan, c2Scan, meetingRoomScan]
    
    def run(self):
        self.after(int(1000/self.fps), self.run)

    def key(self, event):
        # print("pressed", repr(event.char))
        key = event.char
        dx = 0
        dy = 0
        if key == 'w':
            dy = -30
        elif key == 's':
            dy = 30
        elif key == 'a':
            dx = -30
        elif key == 'd':
            dx = 30
        elif key == 'b':
            self.player.transfer(self.canvas)
        self.player.x += dx
        self.player.y += dy
        self.canvas.move(self.player.canvas, dx, dy)
        # '\r'      entry
        # ' '       space
        # '\x1b'    esc
        # '\uf700'  up
        # '\uf701'  down
        # '\uf702'  left
        # '\uf703'  right
