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
        character.canvases.append(self.create_image(
            character.x, 
            character.y, 
            image=character.image
        ))
        self.create_text(
            character.x, 
            character.y + 60, 
            fill = "white", 
            font = "Times 20 italic bold", 
            text = character.name
        )
        self.create_text(
            character.x,
            character.y - 60,
            fill = "white",
            font = "Times 20 italic bold",
            text = "LV. " + character.level
        )

    def drawImage(self, imageObject):
        image = self.create_image(
            imageObject.x,
            imageObject.y,
            image = imageObject.image
        )
        imageObject.canvas = image
    
    def drawText(self, textObject):
        text = self.create_text(
            textObject.x,
            textObject.y,
            fill = "white", 
            font = "Times 20 italic bold", 
            text = textObject.text
        )
        textObject.canvas = text

    def drawItem(self, item):
        item.canvas = self.create_image(
            item.x,
            item.y,
            image=item.image
        )

    def reset(self):
        self.delete("all")
