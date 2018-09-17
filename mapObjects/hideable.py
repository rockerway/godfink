class Hideable:
    def __init__(self):
        self.itemID = None
        self.hideItem = None
        self.showItem = None

    def hide(self):
        self.hideItem(self.itemID)

    def show(self):
        self.showItem(self.itemID)