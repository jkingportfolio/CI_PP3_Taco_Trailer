import gspread
from google.oauth2.service_account import Credentials
import pyfiglet

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
        place_order = input("Enter yes or no:\n")
        place_order = place_order.upper()

        if place_order == 'YES':
            print()
            delivery_type()
            break
        elif place_order == 'NO':
            print()
            thank_you()
            break
        else:
            print('Please enter a valid input')


def admin_access():
    """
    Password to access admin area where prices
    can be updated and tables of sales generated
    """
    print('Test worked')


def delivery_type():
    """
    Determine delivery type
    """
    print('Is this order for delivery or collection?')
    while True:
        delivery_method = input('Please enter delivery or collection: \n')
        delivery_method = delivery_method.upper()
        if delivery_method == 'DELIVERY':
            return delivery_method
        elif delivery_method == 'COLLECTION':
            return delivery_method
        else:
            print('Please enter a valid input.')


def display_menu():
    """
    Display the menu
    """


def order_item():
    """
    Order function
    """


def preview_order():
    """
    Preview order so far function
    """


def print_order():
    """
    Function to print order
    """


def append_sales():
    """
    Function to add sold items and value to google sheets
    """


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
