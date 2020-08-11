import config
import check
import protection


from colorama import init, Fore, Back, Style
init()

password = ''
email = ''


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
