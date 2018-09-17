from actions.actable import Actable


class MapObject(Actable):
    def __init__(self, xRatio, yRatio):
        self.canvas = None
        self.xRatio = xRatio
        self.yRatio = yRatio
