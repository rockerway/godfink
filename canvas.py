import tkinter
from entities.imageInfo import ImageInfo
from entities.textInfo import TextInfo

class Canvas(tkinter.Canvas):
    def __init__(self, master, width, height):
        self.width = width
        self.height = height
        super().__init__(master=master, width=self.width, height=self.height)
        self.pack()

    def setBackground(self, image):
        self.create_image(int(self.width/2), int(self.height/2), image=image)

    def drawCharacter(self, character):
        imageInfo = ImageInfo(
            character.x,
            character.y,
            character.image
        )
        character.canvases.append(self.drawImage(imageInfo))

        if character.name:
            nameInfo = TextInfo(
                character.x,
                character.y + 60,
                "%s - %s" %(character.role, character.name)
            )
            levelInfo = TextInfo(
                character.x,
                character.y - 60,
                "LV. %s" %character.level
            )

            character.canvases.append(self.drawText(nameInfo))
            character.canvases.append(self.drawText(levelInfo))

    def drawImage(self, imageInfo):
        return self.create_image(
            imageInfo.x,
            imageInfo.y,
            image = imageInfo.image
        )
    
    def drawText(self, textInfo):
        return self.create_text(
            textInfo.x,
            textInfo.y,
            fill = "white", 
            font = "Times 20 italic bold", 
            text = textInfo.text
        )

    def drawListbox(self, listboxObject):
        listbox = tkinter.Listbox(self, width=listboxObject.width, height=listboxObject.height)
        return self.create_window(
            int(self.width * listboxObject.xRatio),
            int(self.height * listboxObject.yRatio),
            window=listbox)

    def drawInput(self, textObject):
        text = tkinter.Text(self, width=textObject.width, height=textObject.height)
        return self.create_window(
            int(self.width * textObject.xRatio), 
            int(self.height * textObject.yRatio), 
            window=text)

    def drawButton(self, buttonObject):
        button = tkinter.Button(self, text=buttonObject.text, command=buttonObject.command)
        return self.create_window(
            int(self.width * buttonObject.xRatio), 
            int(self.height * buttonObject.yRatio), 
            window=button)

    def reset(self):
        self.delete("all")
