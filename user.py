from google_sheet import *


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


def validate_address() -> str:
    """
    Function to accept and validate user input for address.
    """
    while True:
        address_number = input(
            'Please enter your house number: \n').strip()
        if address_number.isdigit():
            address_number = int(address_number)
            break
        else:
            clear_screen()
            print(colored(
                f'Im sorry "{address_number}" is not a number.'
                ' Please enter a valid number.\n', 'yellow'))
    clear_screen()
    while True:
        address_street = input('Please enter your street name: \n')
        if address_street != '' and all(chr.isalpha()
                                        or chr.isspace()
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
        first_name = input('Please enter your first name: \n').strip()
        if first_name.isalpha():
            break
        else:
            clear_screen()
            print(colored(
                f'Im sorry "{first_name}" contains numbers or'
                ' special characters,'
                ' please enter a valid name.\n', 'yellow'))
    clear_screen()
    while True:
        surname = input('Please enter your surname: \n').strip()
        if surname.isalpha():
            break
        else:
            clear_screen()
            print(colored(
                f'Im sorry "{surname}" contains numbers or special characters,'
                ' please enter a valid surname.\n', 'yellow'))
    _name = (f'{first_name} {surname}')
    return _name
