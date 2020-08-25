# Importing some other files
import config
import check
import main


# Importing some modules
from colorama import init, Fore, Back, Style
import pyautogui
from pynput.keyboard import Listener
init()


# Some variables
#SomeKeyPressed = False
listener = Listener()


#def loopChecking():
    #global SomeKeyPressed
    # Checking in infinite loop, if is some was key pressed
    #while True:
        #if SomeKeyPressed == True:
            # Function from check.py, to check password
            #check.checkingPassword()
        #pass
    #if SomeKeyPressed == True:
        #check.checkingPassword()
        #SomeKeyPressed = False
    #return SomeKeyPressed

#loopChecking()

def on_press(key):
    # On pressing some key, SomeKeyPressed becomes True
    #SomeKeyPressed = True
    listener.stop()
    print('[LOG] Some key was pressed!')
    check.checkingPassword()


def on_release(key):
    # Just function for pynput
    pass


# Starting protection
def protection():
    #while True:
        # Moving cursor to the matched points (also in infinite loop)
        #pyautogui.move(600, 600)
        try:
            # Listening to the keyboard input
           with Listener(on_press=on_press, on_release=on_release) as listener:
               listener.join()
        except:
            # If some problem causes
            print(Fore.RED + 'Some error was occurupted while checking keyboard interrupt!')
            print(Fore.GREEN + "")
