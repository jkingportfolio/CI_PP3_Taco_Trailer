from termcolor import colored
from google_sheet import *
from taco_trailer_command_line import clear_screen


class User:
    """
    Class to create new user instance.
    """

    def __init__(self, user_name, password,
                 _name, _address):
        self.user_name = user_name
        self.password = password
        self._name = _name
        self._address = _address

    def append_user(self):
        """
        Function to append new user credentials to
        google sheets 'Users' worksheet.
        """
        append_order_data = [self.user_name,
                             self.password,
                             self._name,
                             self._address]
        worksheet_to_update = SHEET.worksheet('Users')
        worksheet_to_update.append_row(append_order_data)


def validate_address(message) -> str:
    """
    Function to accept and validate user input for address.
    """
    while True:
        address_number = input(
            'Please enter your house number. Or enter [Q] to quit.\n').strip()
        if address_number.isdigit():
            address_number = int(address_number)
            break
        elif address_number.capitalize() == 'Q':
            clear_screen()
            print(
                colored(f'Are you sure you want to'
                        f' cancel and return to {message}?', 'yellow'))
            while True:
                confirm_exit = input('\n[Y] - Yes\n[N] - No\n')
                if confirm_exit.capitalize() == 'Y':
                    address_input = 'exit_function'
                    return address_input
                elif confirm_exit.capitalize() == 'N':
                    clear_screen()
                    break
                else:
                    clear_screen()
                    print(colored('Are you sure you want to quit'
                          ' to the main page?', 'yellow'))
                    print('\n[Y] - Yes\n[N] - No')
                    print(colored(f'\nIm sorry but "{confirm_quit}'
                          ' is not a valid option. Please'
                                  ' enter a valid input.\n', 'yellow'))
        else:
            clear_screen()
            print(colored(
                f'Im sorry "{address_number}" is not a number.'
                ' Please enter a valid number.\n', 'yellow'))
    clear_screen()
    while True:
        address_street = input('Please enter your street name. Or enter'
                               ' [Q] to quit.\n')
        if address_street.capitalize() == 'Q':
            clear_screen()
            print(
                colored('Are you sure you want to cancel'
                        ' and return to the main page?', 'yellow'))
            while True:
                confirm_exit = input('\n[Y] - Yes\n[N] - No\n')
                if confirm_exit.capitalize() == 'Y':
                    address_input = 'exit_function'
                    return address_input
                elif confirm_exit.capitalize() == 'N':
                    clear_screen()
                    break
        elif address_street != '' and all(chr.isalpha() or chr.isspace()
                                          for chr in address_street):
            break
        else:
            clear_screen()
            print(colored(
                f'Im sorry "{address_street}" contains numbers or'
                ' special characters, please enter a'
                ' valid street name.\n', 'yellow'))
    _address = (f'{address_number} {address_street}')
    return _address


def validate_name() -> str:
    """
    Function to accept and validate user input for name.
    """
    while True:
        first_name = input('Please enter your first name.'
                           ' Or enter [Q] to quit.\n').strip()
        if first_name.capitalize() == 'Q':
            clear_screen()
            print(colored('Are you sure you want to'
                          ' quit to the main page?', 'yellow'))
            print('\n[Y] - Yes\n[N] - No\n')
            while True:
                confirm_quit = input('Please enter a valid input: \n').strip()
                if confirm_quit.capitalize() == 'Y':
                    clear_screen()
                    return False
                elif confirm_quit.capitalize() == 'N':
                    clear_screen()
                    break
                else:
                    clear_screen()
                    print(colored('Are you sure you want to quit'
                          ' to the main page?', 'yellow'))
                    print('\n[Y] - Yes\n[N] - No')
                    print(colored(f'\nIm sorry but "{confirm_quit}'
                          ' is not a valid option. Please'
                                  ' enter a valid input.\n', 'yellow'))
        elif first_name.isalpha() and first_name.capitalize() != 'Q':
            break
        else:
            clear_screen()
            print(colored(
                f'Im sorry "{first_name}" contains numbers or'
                ' special characters,'
                ' please enter a valid name.\n', 'yellow'))
    clear_screen()
    while True:
        surname = input('Please enter your surname.'
                        ' Or enter [Q] to quit.\n').strip()
        if surname.capitalize() == 'Q':
            clear_screen()
            print(colored('Are you sure you want to'
                          ' quit to the main page?', 'yellow'))
            print('\n[Y] - Yes\n[N] - No\n')
            while True:
                confirm_quit = input('Please enter a valid input: \n').strip()
                if confirm_quit.capitalize() == 'Y':
                    clear_screen()
                    return False
                elif confirm_quit.capitalize() == 'N':
                    clear_screen()
                    break
                else:
                    clear_screen()
                    print(colored('Are you sure you want to quit'
                          ' to the main page?', 'yellow'))
                    print('\n[Y] - Yes\n[N] - No')
                    print(colored(f'\nIm sorry but "{confirm_quit}'
                          ' is not a valid option. Please'
                                  ' enter a valid input.\n', 'yellow'))
        elif surname.isalpha() and surname.capitalize() != 'Q':
            break
        else:
            clear_screen()
            print(colored(
                f'Im sorry "{surname}" contains numbers or special characters,'
                ' please enter a valid surname.\n', 'yellow'))
    clear_screen()
    _name = (f'{first_name} {surname}')
    return _name
