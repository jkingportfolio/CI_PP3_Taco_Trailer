"""
Google sheets module
"""
from tabulate import tabulate
from termcolor import colored
import gspread
from google.oauth2.service_account import Credentials
from taco_trailer_command_line import clear_screen

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
PASSWORD = SHEET.worksheet("Password").acell('A1').value
LOGINS = SHEET.worksheet('Users').get_all_records()


def user_name_list():
    USER_NAMES = []
    for login in LOGINS:
        USER_NAMES.append((login.get('User Name')))
    return USER_NAMES


def validate_new_username(new_username):
    USER_NAMES = user_name_list()
    if new_username in USER_NAMES:
        clear_screen()
        print(colored(f'Username "{new_username}" is already taken.\n','yellow'))
        return False
    elif ' ' in new_username:
        clear_screen()
        print(colored(f'Username "{new_username}" cannot be created as it has whitespaces.\n','yellow'))
        return False
    else:
        clear_screen()
        print(colored(f'Username "{new_username}" is valid and created\n','green'))
        USER_NAMES.append(new_username)
        return True
