"""
Library of Command Line functions
"""
import os
from time import sleep
from termcolor import colored

PASSWORD_CRITERIA = ('Password creation criteria.\n\nPasswords must:'
                     ' \n\n1. Be longer than 6 characters\n'
                     '2. Be less than 20 characters\n'
                     '3. Include at least one numeral\n'
                     '4. Include at least one uppercase letter\n'
                     '5. Include at least one lowercase letter\n'
                     '6. Include at lease one of the following'
                     ' characters: $ @ #\n'
                     '7. Not include any whitespaces\n')


def clear_screen():
    """
    Function to clear screen.
    """
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


def load_animation(message: str):
    """
    Function to simulate a loading screen with passed argument.
    @param message(string): Custom loading message.
    """
    clear_screen()
    load_message = (colored(message, 'green'))
    for i in range(5):
        print(load_message)
        sleep(0.75)
        load_message = load_message + (colored('.', 'green'))
        clear_screen()


def validate_password(passwd: str):
    """
    Function to validate user password creation - credits to geeksforgeeks.org
    @param passwd(string): Password as entered by user input.
    """

    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        print(colored('Password length should be at least 6.\n', 'yellow'))
        val = False

    if len(passwd) > 20:
        print(colored('Password length should be not be'
                      ' greater than 8.\n', 'yellow'))
        val = False

    if not any(char.isdigit() for char in passwd):
        print(colored('Password should have at least one'
                      ' numeral.\n', 'yellow'))
        val = False

    if not any(char.isupper() for char in passwd):
        print(colored('Password should have at least one'
                      ' uppercase letter.\n', 'yellow'))
        val = False

    if not any(char.islower() for char in passwd):
        print(colored('Password should have at least one lowercase'
                      ' letter.\n', 'yellow'))
        val = False

    if not any(char in SpecialSym for char in passwd):
        print(colored('Password should have at least one of the '
                      'symbols $ @ #\n', 'yellow'))
        val = False

    if ' ' in passwd:
        print(colored('Password cannot contain spaces.', 'yellow'))
        val = False
    if val:
        return val
