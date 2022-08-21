"""
Main python file
"""
import os
import getpass
import gspread
from google.oauth2.service_account import Credentials
import pyfiglet
from tabulate import tabulate
from time import sleep
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

menu = SHEET.worksheet("Menu").get_all_values()
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
            'Please enter a valid input (Yes/No) or for'
            ' Admin Access enter(Admin).\n')
        place_order = place_order.upper()

        if place_order == 'YES':
            clear_screen()
            customer_details()
            break
        elif place_order == 'NO':
            clear_screen()
            thank_you()
            break
        elif place_order == 'ADMIN':
            admin_access()
            break


def customer_details():
    """
    Collect user details via input
    """
    global name
    global delivery_type
    global address

    print('We would like to take your details.\n')
    while True:
        name = input('Please enter your name: ')
        if name.isalpha():
            print(f'\nHi {name}!\n')
            break
        else:
            print(
                '\nPlease enter a valid name that does not'
                ' contain numbers or special characters\n')
    while True:
        delivery_type = input('Please enter your delivery'
                              ' type (Delivery/Collection): ')
        delivery_type = delivery_type.upper()
        if delivery_type == 'DELIVERY':
            print()
            print(
                f'You selected {delivery_type.capitalize()} for your order.\n')
            address = input('Please enter your address: ')
            break
        elif delivery_type == 'COLLECTION':
            print()
            print(
                f'You selected {delivery_type.capitalize()} for your order.\n')
            address = 'The Taco Trailer'
            break
        else:
            print()
            print('Please enter a valid input.\n')

    clear_screen()
    print('Thank you for your details!\n')
    print('Loading our menu...\n')
    sleep(2)
    clear_screen()
    display_menu()


def display_menu():
    """
    Display the menu
    """
    menu = SHEET.worksheet("Menu").get_all_values()
    print(tabulate(menu, headers=[
          'Item', 'Name', 'Cost (£)'], tablefmt="simple", numalign="center"))
    print()
    order_item()


def order_item():
    """
    Order function
    """
    food_item = input('Please enter a valid input? ')

    while True:
        food_item = food_item.upper()
        if food_item == "Q":
            quit = input(
                'Are you sure you want to cancel the order? (Yes/No)\n')
            quit = quit.upper()
            if quit == 'YES':
                order_list.clear()
                clear_screen()
                thank_you()
                sleep(2)
                clear_screen()
                welcome()
                break
            elif quit == 'NO':
                order_item()
                break
            else:
                print('Im sorry i need a valid input')
        elif food_item == "NO":
            complete_order()
            break
        elif food_item == '*':
            remove_item()
            break
        elif food_item.isdigit():
            try:
                food_item = int(food_item) - 1
                order_list.append(menu[food_item])
                this_item = (menu[food_item])
                print(
                    f'You ordered Item {this_item[0]}, {this_item[1]}'
                    ' priced at {this_item[2]}\n')
                food_item = input('What other item would you like? ')
            except IndexError:
                print(
                    f'Im sorry Item {food_item + 1} does not exist.'
                    ' Please enter a valid item number')
                order_item()
                break
        else:
            print(
                f'Im sorry but {food_item.capitalize()} is not a menu'
                ' option. Please enter a valid input')
            order_item()
            break


def remove_item():
    """
    Pop last item added to menu
    """
    removed_item = order_list[-1]
    print(f'you have removed {removed_item} from your order')
    order_list.pop()
    print(order_list)
    order_item()


def complete_order():
    """
    Function to complete order and arguments to Order class and its functions
    """
    print('Are ready to complete your order?\n')
    while True:
        order_complete = input('Yes, No, Cancel Order ')
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
                    f'Incorrect password. Remaining password'
                    f' attempts {password_guesses}\n')
            elif password_guesses == 0:
                print(
                    'Im sorry you have guessed wrong more than 3 times\n')
                welcome()


def clear_screen():
    """
    Function to clear screen
    """
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


def thank_you():
    """
    Function to add sold items and value to google sheets
    """
    title = 'Thanks for visiting!'
    print(pyfiglet.figlet_format(title))


def main():
    """
    Run all program functions
    """
    welcome()


main()
