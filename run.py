"""
Main python file
"""
import getpass
import gspread
from google.oauth2.service_account import Credentials
import pyfiglet
import pandas as pd

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


def display_menu():
    """
    Display the menu
    """
    print('Now this will show the menu\n')
    menu = SHEET.worksheet("Menu").get_all_values()
    menu_df = pd.DataFrame(menu, columns=['Item', 'Name', 'Cost'])
    print(f'{menu_df}\n')
    order_item()


def order_item():
    """
    Order function
    """
    order = []
    food_item = input('What would you like to order? ')

    while True:
        food_item = food_item.upper()
        if food_item == "Q":
            break
        elif food_item == "NO":
            delivery_type()
            # preview_order(order)
            break
        else:
            print(food_item)
            order.append(food_item)
            food_item = input('What other item would you like? ')


def delivery_type():
    """
    Determine delivery type
    """
    print('Is this order for Delivery or Collection?\n')
    while True:
        delivery_method = input('Please enter delivery or collection: \n')
        delivery_method = delivery_method.upper()
        if delivery_method == 'DELIVERY':
            print()
            print(
                f'You selected {delivery_method.capitalize()} for your order.')
            preview_order(order)
            break
        elif delivery_method == 'COLLECTION':
            print()
            print(
                f'You selected {delivery_method.capitalize()} for your order.')
            preview_order(order)
            break
        else:
            print()
            print('Please enter a valid input.')
    return delivery_method


def preview_order(order):
    """
    Preview order so far function
    """
    print(f'\nYou ordered {order}')
    while True:
        order_more = input('Would you like to add to your order? ')
        if order_more == 'Yes':
            order_item()
            break
        elif order_more == 'No':
            print_order(order)
            break
        else:
            print('That is not a valid input')


def print_order(order):
    """
    Function to print order
    """
    print('passed to print order function succesfully')
    print(order)
    append_sales(order)


def append_sales(order):
    """
    Function to add sold items and value to google sheets
    """
    worksheet_to_update = SHEET.worksheet('Sales')
    worksheet_to_update.append_row(order)
    print("worksheet updated successfully\n")


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
