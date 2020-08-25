import config
import check
import protection
import main


from colorama import init, Fore, Back, Style
init()

# Some variables
option = ''
password = 'defaultPass201'
email = 'osabfisa@gmail.com'


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
    main.checkOption()


def change():
    print('New password: ')
    password = input()
    print('Your new password: ' + password)
    print('New email: ')
    email = input()
    print('Your new email: ' + email)
    main.checkOption()
