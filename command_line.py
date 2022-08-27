"""
Library of Command Line functions
"""
import os


def clear_screen():
    """
    Function to clear screen
    """
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
