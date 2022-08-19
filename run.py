"""
Main python file
"""
import getpass
import gspread
from google.oauth2.service_account import Credentials
import pyfiglet
import pandas as pd
import order

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('taco_trailer')


def welcome():
    """
    Display welcome message
    """

    title = 'Welcome to the Taco Trailer'
    print(pyfiglet.figlet_format(title))
    print('Hello, would you like to place an order?\n')
    while True:
        place_order = input(
            "Please enter Yes or No. Or for Admin Access enter 'Admin':\n")
        place_order = place_order.upper()

        if place_order == 'YES':
            print()
            display_menu()
            break
        elif place_order == 'NO':
            print()
            thank_you()
            break
        elif place_order == 'ADMIN':
            admin_access()
            break
        else:
            print('Please enter a valid input')
            

def display_menu():
    """
    Display the menu
    """

    print('Now this will show the menu\n')
    menu = SHEET.worksheet("Menu").get_all_values()
    menu_df = pd.DataFrame(menu, columns=['Item', 'Name', 'Cost'])
    print(f'{menu_df}\n')
    # order_item()


def admin_access():
    """
    Password to access admin area where prices
    can be updated and tables of sales generated
    """
    password_guesses = 3
    while True:
        admin_password = getpass.getpass("Please enter Admin Password:\n")

        if admin_password == 'TACOtrailer':
            print('Access granted')
            break
        else:
            password_guesses -= 1
            if password_guesses > 0:
                print(
                    f'Incorrect password. Remaining password \
                    attempts {password_guesses}\n')
            elif password_guesses == 0:
                print(
                    'Im sorry you have guessed wrong more than 3 times\n')
                welcome()


def thank_you():
    """
    Function to add sold items and value to google sheets
    """
    title = 'Thanks for visting!'
    print(pyfiglet.figlet_format(title))


def main():
    """
    Run all program functions
    """
    welcome()


main()
