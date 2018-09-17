class InputInfo:
    def __init__(self, xRatio, yRatio, width, height, callback=None, withScrollBar=False):
        self.xRatio = xRatio
        self.yRatio = yRatio
        self.width = width
        self.height = height
        self.callback = callback
        self.withScrollBar = withScrollBar