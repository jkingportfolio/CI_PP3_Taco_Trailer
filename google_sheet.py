"""
Google sheets module
"""
from time import sleep
from tabulate import tabulate
from termcolor import colored
import pyfiglet
import gspread
import pwinput
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
LOGINS = SHEET.worksheet('Users').get_all_records()


def generate_order_number(worksheet):
    """
    Function to parse google sheets sales worksheet
    to find next row, this row is the current
    order number.
    @param worksheet(string): Worksheet in which to parse.
    """
    row_list = list(filter(None, worksheet.col_values(1)))
    return str(len(row_list)+1)


def user_name_list() -> list:
    """
    Function to parse google sheets 'Users' worksheet and generate
    a list of all current users.
    """
    USER_NAMES = []
    for login in LOGINS:
        USER_NAMES.append((login.get('User Name')))
    return USER_NAMES


def validate_new_username(new_username: str) -> bool:
    """
    Function to validate a new username and check if already exists
    in the google sheets worksheet.
    @param new_username(string): User name as entered by user input.
    """
    USER_NAMES = user_name_list()
    if new_username in USER_NAMES:
        clear_screen()
        print(
            colored(f'Username "{new_username}" is already'
                    ' taken.\n', 'yellow'))
        return False
    elif ' ' in new_username:
        clear_screen()
        print(colored(
            f'Username "{new_username}" cannot be created as'
            ' it has whitespaces.\n', 'yellow'))
        return False
    else:
        clear_screen()
        print(
            colored(f'Username "{new_username}" is valid and'
                    ' created\n', 'green'))
        USER_NAMES.append(new_username)
        return True


def change_password(member_number: str):
    """
    Function to accept user input to change user password.
    @param member_number(string): Member number as taken
    from google sheet worksheets row
    """
    current_password = LOGINS[member_number].get('Password')
    member_cell_number = member_number + 2
    cancel_prompt = ('Are you sure you want to cancel'
                     ' password change and return to members area?')
    password_guesses = 3
    while True:
        print(colored('Change password\n', 'green'))
        print(
            'Please enter your current password or enter "Q"'
            ' to cancel password change: \n')
        password_input = pwinput.pwinput(
            'Password: ')
        if password_input == current_password:
            clear_screen()
            print(colored('Current password entered correct.\n', 'green'))
            while True:
                print(
                    'Please enter your new password, or enter "Q"'
                    ' to cancel password change: \n')
                new_password = pwinput.pwinput(
                    'Password: ')
                clear_screen()
                if validate_password(new_password):
                    clear_screen()
                    while True:
                        print(colored('New password entered has'
                                      ' passed validation.\n', 'green'))
                        print(
                            'Please confirm your new password, or'
                            ' enter "Q" to quit: \n')
                        confirm_password = pwinput.pwinput(
                            'Password: ')
                        clear_screen()
                        if confirm_password == new_password:
                            SHEET.worksheet('Users').update_cell(
                                member_cell_number, 2, new_password)
                            clear_screen()
                            print(pyfiglet.figlet_format('Password updated.'))
                            print(colored(
                                '\nPlease note changes will only take place'
                                ' upon program restart', 'green'))
                            sleep(5)
                            clear_screen()
                            break
                        elif confirm_password.capitalize() == 'Q':
                            confirm_exit = cancel_current_option(cancel_prompt)
                            if not confirm_exit:
                                return
                        else:
                            print(
                                colored('Second password entry did not meet'
                                        ' the first.\n', 'yellow'))
                    break
                elif new_password.capitalize() == 'Q':
                    confirm_exit = cancel_current_option(cancel_prompt)
                    if not confirm_exit:
                        return
            break
        elif password_input.capitalize() == 'Q':
            confirm_exit = cancel_current_option(cancel_prompt)
            if not confirm_exit:
                return

        else:
            password_guesses -= 1
            if password_guesses > 0:
                clear_screen()
                print(colored(
                    f'Incorrect password. Remaining password'
                    f' attempts {password_guesses}\n', 'yellow'))
            elif password_guesses == 0:
                clear_screen()
                print(colored('For security reasons we are cancelling'
                              ' this password change request!', 'yellow'))
                sleep(5)
                clear_screen()
                break


def cancel_current_option(prompt: str):
    """
    Function to control Quit option in current program position.
    @param prompt(string): Custom prompt string to populate
    function text.
    """
    while True:
        clear_screen()
        print(
            colored(f'{prompt}', 'yellow'))
        confirm_exit = input('\n[Y] - Yes\n[N] - No\n')
        if confirm_exit.capitalize() == 'Y':
            clear_screen()
            return False
        elif confirm_exit.capitalize() == 'N':
            clear_screen()
            return True
        else:
            print(
                f'Im sorry but "{confirm_exit}" is not a valid'
                ' option. Please enter a valid option')
