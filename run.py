"""
Main python file
"""
import getpass
import gspread
from google.oauth2.service_account import Credentials
import pyfiglet
import pandas as pd
from order import Order

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('taco_trailer')

order_list = []
name = None
delivery_type = None
address = None


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
            customer_details()
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


def customer_details():
    """
    Collect user details via input
    """
    global name
    global delivery_type
    global address

    print('We would like to take your details.')
    while True:
        name = input('Please enter your name: ')
        if name.isalpha():
            print(f'Hi {name}!')
            break
        else:
            print(
                'Please enter a valid name that does not contain numbers or special characters')
    while True:
        delivery_type = input('Please enter your delivery type: ')
        delivery_type = delivery_type.upper()
        if delivery_type == 'DELIVERY':
            print()
            print(
                f'You selected {delivery_type.capitalize()} for your order.')
            break
        elif delivery_type == 'COLLECTION':
            print()
            print(
                f'You selected {delivery_type.capitalize()} for your order.')
            break
        else:
            print()
            print('Please enter a valid input.')
    address = input('Please enter your address: ')
    print('Thank you for your details!\n')
    display_menu()


def display_menu():
    """
    Display the menu
    """
    print('Please take a look at our menu!\n')
    menu = SHEET.worksheet("Menu").get_all_values()
    menu_df = pd.DataFrame(menu, columns=['Item', 'Name', 'Cost'])
    print(f'{menu_df}\n')
    order_item()


def order_item():
    """
    Order function
    """
    food_item = input('What would you like to order? ')

    while True:
        food_item = food_item.upper()
        if food_item == "Q":
            quit = input('Are you sure you want to cancel the order?')
            quit = quit.upper()
            if quit == 'YES':
                welcome()
            elif quit == 'NO':
                order_item()
                break
            else:
                print('Im sorry i need a valid input')
        elif food_item == "NO":
            complete_order()
            break
        else:
            print(food_item)
            order_list.append(food_item)
            print(order_list)
            food_item = input('What other item would you like? ')


def complete_order():
    global name
    global delivery_type
    global address
    global order_list
    print('Are ready to complete your order?\n')
    while True:
        order_complete = input('Yes, No, Cancel Order')
        order_complete = order_complete.upper()
        if order_complete == 'YES':
            this_order = Order(name, delivery_type, address, order_list)
            this_order.print_receipt()
            break
        elif order_complete == 'NO':
            order_item()
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
