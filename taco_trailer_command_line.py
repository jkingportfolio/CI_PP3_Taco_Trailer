"""
Library of Command Line functions
"""
import os
from time import sleep

password_criteria = ('Password creation criteria.\n\nPasswords must: \n\n1. Be longer than 6 characters\n'
                     '2. Be less than 20 characters\n'
                     '3. Include at least one numeral\n'
                     '4. Include at least one uppercase letter\n'
                     '5. Include at least one lowercase letter\n'
                     '6. Include at lease one of the following characters: $ @ #\n'
                     '7. Not include any whitespaces\n')


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
        print('Password length should be at least 6.\n')
        val = False

    if len(passwd) > 20:
        print('Password length should be not be greater than 8.\n')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral.\n')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter.\n')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter.\n')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $ @ #\n')
        val = False

    if ' ' in passwd:
        print('Password cannot contain spaces.')
        val = False
    if val:
        return val
