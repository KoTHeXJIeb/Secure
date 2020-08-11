import config
import check
import protection


# Importing some modules
from colorama import init, Fore, Back, Style
import pyautogui
from pynput.keyboard import Listener
init()


# Some variables
isSomeKeyPressed = False


def on_press(key):
    #print(Fore.GREEN + 'Wow, some key was pressed!')
    if key == 'Space':
        print('Magic?')
    else:
        isSomeKeyPressed == True
        print('Some key was pressed!')


def loopChecking():
    while True:
        if isSomeKeyPressed == True:
            print('Is that working?')
            isSomeKeyPressed = False


loopChecking()


def on_release(key):
    #print(Fore.GREEN + 'Wow, some key was released!')
    pass

def protection():
    while True:
        #pyautogui.move(600, 600)
        try:
           with Listener(on_press=on_press, on_release=on_release) as listener:
               listener.join()
        except:
            print(Fore.RED + 'Some error was occurupted while checking keyboard interrupt!')
