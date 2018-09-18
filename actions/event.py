class Event:
    def __init__(self, eventInfo):
        self.levelLimit = eventInfo.levelLimit
        self.keyword = eventInfo.keyword
        self.info = eventInfo.info
        self.validate = eventInfo.validate
        self.validateSeparator = eventInfo.validateSeparator
        self.lv = eventInfo.lv
