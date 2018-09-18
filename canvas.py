import tkinter
from tkinter import font
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
        character.effect = self.drawImage(ImageInfo(
            character.x,
            character.y,
            character.effectImage
        ))
        character.canvases.append(character.effect)
        self.itemconfig(character.effect, state=tkinter.HIDDEN)
        character.canvases.append(self.drawImage(ImageInfo(
            character.x,
            character.y,
            character.image
        )))

        if character.name:
            nameInfo = TextInfo(
                character.x,
                character.y + 60,
                "%s - %s" % (character.role, character.name)
            )
            levelInfo = TextInfo(
                character.x,
                character.y - 60,
                "LV. %s" % character.level
            )

            character.canvases.append(self.drawText(nameInfo))
            character.canvases.append(self.drawText(levelInfo))

    def drawImage(self, imageInfo):
        return self.create_image(
            imageInfo.x,
            imageInfo.y,
            image=imageInfo.image
        )

    def drawText(self, textInfo, startFrom=tkinter.CENTER):
        textFont = font.Font(family='Fixdsys', size=16)
        return self.create_text(
            textInfo.x,
            textInfo.y,
            fill="white",
            font=textFont,
            text=textInfo.text,
            anchor=startFrom
        )

    def drawRadio(self, radioObject):
        radioObject.frame = tkinter.Frame()
        radioObject.canvas = tkinter.Radiobutton(
            radioObject.frame,
            text=radioObject.text,
            variable=radioObject.var,
            value=radioObject.value)
        radioObject.canvas.pack(anchor=tkinter.N)
        radioObject.itemID = self.create_window(
            int(self.width * radioObject.xRatio),
            int(self.height * radioObject.yRatio),
            window=radioObject.frame)
        radioObject.hideItem = self.hideItem
        radioObject.showItem = self.showItem

    def drawInput(self, textObject, startFrom=tkinter.CENTER, canModify=True):
        inputFont = font.Font(family='Fixdsys', size=16)
        textObject.frame = tkinter.Frame()
        state = tkinter.NORMAL
        if not canModify:
            state = tkinter.DISABLED
        textObject.canvas = tkinter.Text(
            textObject.frame,
            width=textObject.width,
            height=textObject.height,
            font=inputFont,
            state=state)
        if textObject.withScrollBar:
            textObject.scrollBar = tkinter.Scrollbar(textObject.frame)
            textObject.scrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
            textObject.scrollBar['command'] = textObject.canvas.yview()
            textObject.canvas['yscrollcommand'] = textObject.scrollBar.set
        textObject.canvas.pack(expand=1, fill=tkinter.BOTH)
        if textObject.command:
            textObject.canvas.bind("<Key>", textObject.command)
        textObject.itemID = self.create_window(
            int(self.width * textObject.xRatio),
            int(self.height * textObject.yRatio),
            window=textObject.frame,
            anchor=startFrom)
        textObject.hideItem = self.hideItem
        textObject.showItem = self.showItem

    def drawButton(self, buttonObject):
        buttonObject.canvas = tkinter.Button(
            self, text=buttonObject.text, command=buttonObject.command)
        buttonObject.itemID = self.create_window(
            int(self.width * buttonObject.xRatio),
            int(self.height * buttonObject.yRatio),
            window=buttonObject.canvas)
        buttonObject.hideItem = self.hideItem
        buttonObject.showItem = self.showItem

    def showItem(self, itemID):
        self.itemconfig(itemID, state=tkinter.NORMAL)

    def hideItem(self, itemID):
        self.itemconfig(itemID, state=tkinter.HIDDEN)

    def reset(self):
        self.delete("all")

    def deleteWeight(self, weight):
        self.delete(weight)
