# Import some files
import config
import check
import protection


# Importing nessasary modules
from subprocess import call
from colorama import init, Fore, Back, Style
#init


# Some useless variables
option = ''


# Some useless functions
print(Fore.GREEN + 'Welcome to SCP - secure, check, protect')
print('Select the option below: ')
print('1) Configurate')
print('2) Edit password and email')
print('3) Start protection')
print('(Choose from 1 to 3)')
option = int(input())


def startProtection():
    print('Starting protection')
    protection.protection()


def checkOption():
    if option == 1:
        config.show()
        print('[LOG] Opening configuration file')
    if option == 2:
        config.change()
    if option == 3:
        startProtection()


checkOption()


# Is this file contains any important info?
