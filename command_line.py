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
