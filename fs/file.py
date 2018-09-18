from enum import Enum


class ModeType(Enum):
    WRITE = "w"
    READ = "r"
    APPEND = "a"
    WRITEREAD = "r+"


class File:
    @staticmethod
    def read(fileName):
        file = open(fileName, ModeType.READ.value)
        context = file.read()
        file.close()
        return context

    @staticmethod
    def write(fileName, context):
        file = open(fileName, ModeType.WRITE.value)
        file.write(context)
        file.close()
