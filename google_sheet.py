"""
Google sheets module
"""
from tabulate import tabulate
from termcolor import colored
from time import sleep
import pyfiglet
import gspread
import getpass
from google.oauth2.service_account import Credentials
from taco_trailer_command_line import clear_screen, validate_password


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('taco_trailer')

MENU = SHEET.worksheet("Menu").get_all_values()
FORMATTED_MENU = (tabulate(MENU, headers=['Item', 'Name', 'Cost (£)'],
                           tablefmt="simple", numalign="center"))
SALES_WORKSHEET = SHEET.worksheet("Sales")
ORDER_RECORDS = SALES_WORKSHEET.get_all_records()
ORDER_RECORD_VALUES = SALES_WORKSHEET.get_all_values()
# PASSWORD = SHEET.worksheet("Password").acell('A1').value
LOGINS = SHEET.worksheet('Users').get_all_records()


def generate_order_number(worksheet):
    """
    Parse google sheets sales page to find next row, this row is the current order number
    """
    row_list = list(filter(None, worksheet.col_values(1)))
    return str(len(row_list)+1)


def user_name_list():
    USER_NAMES = []
    for login in LOGINS:
        USER_NAMES.append((login.get('User Name')))
    return USER_NAMES


def validate_new_username(new_username):
    USER_NAMES = user_name_list()
    if new_username in USER_NAMES:
        clear_screen()
        print(
            colored(f'Username "{new_username}" is already taken.\n', 'yellow'))
        return False
    elif ' ' in new_username:
        clear_screen()
        print(colored(
            f'Username "{new_username}" cannot be created as it has whitespaces.\n', 'yellow'))
        return False
    else:
        clear_screen()
        print(
            colored(f'Username "{new_username}" is valid and created\n', 'green'))
        USER_NAMES.append(new_username)
        return True


def change_password(member_number):
    current_password = LOGINS[member_number].get('Password')
    print(colored('Change password\n', 'green'))
    member_cell_number = member_number + 2
    while True:
        password_input = getpass.getpass(
            'Please enter your current password: \n')
        if password_input == current_password:
            clear_screen()
            print(colored('Current password entered correct.\n', 'green'))
            while True:
                new_password = getpass.getpass(
                    'Please enter your new password: \n')
                clear_screen()
                if validate_password(new_password):
                    clear_screen()
                    while True:
                        confirm_password = getpass.getpass(
                            'Please confirm your new password: \n')
                        clear_screen()
                        if confirm_password == new_password:
                            password_cell = 'B' + str(member_number)
                            SHEET.worksheet('Users').update_cell(
                                member_cell_number, 2, new_password)
                            clear_screen()
                            print(pyfiglet.figlet_format('Password updated'))
                            sleep(2)
                            clear_screen()
                            break
                        else:
                            print('Second password entry did not meet the first.\n')
                    break
                else:
                    print('Your new password didnt meet the criteria.\n')
            break
        else:
            clear_screen()
            print(colored('Invalid current Password entry\n', 'yellow'))
