import tkinter
import configparser
from app import Application

# init config
config = configparser.ConfigParser()
config.read('config.ini')

def main():
    root = tkinter.Tk()
    root.title('人生如遊戲')

    # check does the window need fixed size
    if config['window']['fixed_size'] == 'yes':
        root.resizable(width=False, height=False)

    application = Application(root)

if __name__ == '__main__':
    main()
