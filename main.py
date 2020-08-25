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
version = 'Beta 0.2'


# Some useless functions
print(Fore.GREEN + 'Welcome to SCP - secure, check, protect')
print('Current version is ' + version)
print('Select the option below: ')
print('1) Configurate')
print('2) Start protection')
print('(Choose from 1 to 2)')
option = int(input())


def startProtection():
    print('Starting protection')
    protection.protection()


def checkOption():
    if option == 1:
        config.chooseConfig()
    if option == 3:
        startProtection()


checkOption()


# Is this file contains any important info?
