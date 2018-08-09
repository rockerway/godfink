import tkinter
from app import Application

fps = 25
width = 0
height = 0

def main():
    root = tkinter.Tk()
    root.title('人生如遊戲')
    root.resizable(width=False, height=False)

    width = root.winfo_screenwidth() - 10
    height = root.winfo_screenheight() - 123
    application = Application(root, width, height, fps)

if __name__ == '__main__':
    main()
