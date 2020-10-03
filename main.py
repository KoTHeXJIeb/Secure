
# Importing nessasary modules
from colorama import init, Fore, Back, Style
import pyautogui
from pynput.keyboard import Listener
init()


# Some useless variables
option = ''
version = 'Beta 0.2'
option = ''
password = 'defaultPass201'
email = 'osabfisa@gmail.com'


listener = Listener()


def on_press(key):
    listener.stop()
    print('[LOG] Some key was pressed!')
    checkingPassword()


def on_release(key):
    # Just function for pynput
    pass


# Starting protection
def startProtection():
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


def checkingPassword():
    # Checking password (REALLY?)
    password = input()

def checkPassword():
    if password in password:
        print(Fore.GREEN + 'Password is correct')
    else:
        print(Fore.RED + 'Your password is incorrect! Try something else?')


def chooseConfig():
    print('Choose the option of config file: ')
    print('1) Show current settings ')
    print('2) Edit current settings ')
    option = int(input())


def optionCheck():
    if option == 1:
        show()
    if option == 2:
        change()


def show():
    print('Your current password is - ' + password)
    print('Your current email is - ' + email)
   


def change():
    print('New password: ')
    password = input()
    print('Your new password: ' + password)
    print('New email: ')
    email = input()
    print('Your new email: ' + email)


# Some useless functions
print(Fore.GREEN + 'Welcome to SCP - secure, check, protect')
print('Current version is ' + version)
print('Select the option below: ')
print('1) Configurate')
print('2) Start protection')
print('(Choose from 1 to 2)')
option = int(input())
if option == 1:
    chooseConfig()
if option == 2:
    startProtection()



# Is this file contains any important info?
