import tkinter

class Canvas(tkinter.Canvas):
    def __init__(self, master, width, height):
        self.width = width
        self.height = height
        super().__init__(master=master, width=self.width, height=self.height)
        self.pack()

    def setBackground(self, image):
        self.create_image(int(self.width/2), int(self.height/2), image=image)

    def drawCharacter(self, character):
        character.canvas = self.create_image(
            character.x, 
            character.y, 
            image=character.image
        )

    def reset(self):
        self.delete("all")
