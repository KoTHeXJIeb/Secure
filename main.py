# Import some files
import config
import check
import protection


# Importing nessasary modules
from colorama import init, Fore, Back, Style
init()


# Some useless variables
option = ''
version = 'Beta 0.2'


# Some useless functions
print(Fore.GREEN + 'Welcome to SCP - secure, check, protect')
print('Current version is ' + version)
print('Select the option below: ')
print('1) Configurate')
print('2) Start protection')
print('(Choose from 1 to 2)')
option = int(input())


def initializeProtection():
    protection.startProtection()


def checkOption():
    if option == 1:
        config.chooseConfig()
    if option == 2:
        initializeProtection()


checkOption()


# Is this file contains any important info?
