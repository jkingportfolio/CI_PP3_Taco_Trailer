"""
Library of Command Line functions
"""
import os
from time import sleep


def clear_screen():
    """
    Function to clear screen
    """
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


def load_animation(message):
    """
    Print to screen processing order 
    """
    clear_screen()
    i = 0
    load_message = message
    for i in range(5):
        print(load_message)
        sleep(0.75)
        load_message = load_message + ('.')
        clear_screen()
        i = + 1


def validate_password(passwd):
    """
    Function to validate user password creation - credits to geeksforgeeks.org
    """

    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        print('length should be at least 6')
        val = False

    if len(passwd) > 20:
        print('length should be not be greater than 8')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val
