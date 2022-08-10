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

def admin_access():
    """
    Password to access admin area where prices
    can be updated and tables of sales generated
    """  


def delivery_type():
    """
    Determine delivery type
    """


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


def main():
    """
    Run all program functions
    """
    welcome()
    print('Testing main function')


main()
