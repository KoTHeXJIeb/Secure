import config
import check
import protection


# Some useless project files
from colorama import init, Fore, Back, Style
init()

def checkingPassword():
    # Checking password (REALLY?)
    config.password = input()

def checkPassword():
    if config.password in config.password:
        print(Fore.GREEN + 'Password is correct')
    else:
        print(Fore.RED + 'Your password is incorrect! Try something else?')
