"""
Main python file
"""
import os
import getpass
from google_sheet import *
import pyfiglet
from time import sleep
from order import Order


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
        place_order = place_order.capitalize()

        if place_order == 'Yes':
            clear_screen()
            customer_details()
            break
        elif place_order == 'No':
            clear_screen()
            thank_you()
            break
        elif place_order == 'Admin':
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
        delivery_type = delivery_type.capitalize()
        if delivery_type == 'Delivery':
            print()
            print(
                f'You selected {delivery_type.capitalize()} for your order.\n')
            address = input('Please enter your address: ')
            break
        elif delivery_type == 'Collection':
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
    print(FORMATTED_MENU)
    order_item()


def generate_order_number(worksheet):
    """
    Parse google sheets sales page to find next row, this will be the order number
    """
    row_list = list(filter(None, worksheet.col_values(1)))
    return str(len(row_list)+1)


def order_item():
    """
    Order function
    """
    instructions = ("\nAdd item by entering item number.\n"
                    "To remove last item enter '*'.\n"
                    "To cancel order enter 'Q'.\n"
                    "To complete order enter 'X'.\n")

    print(instructions)
    food_item = input("Please enter a valid input: ")
    while True:
        food_item = food_item.capitalize()
        if food_item == "Q":
            quit = input(
                'Are you sure you want to cancel the order? (Yes/No)\n')
            quit = quit.capitalize()
            if quit == 'Yes':
                order_list.clear()
                clear_screen()
                thank_you()
                sleep(2)
                clear_screen()
                welcome()
                break
            elif quit == 'No':
                clear_screen()
                print(FORMATTED_MENU)
                print(instructions)
                order_item()
                break
            else:
                print('Im sorry i need a valid input: ')
        elif food_item == "X":
            if len(order_list) == 0:
                clear_screen()
                print(FORMATTED_MENU)
                print(instructions)
                print('\nCannot complete order, basket is empty.\n')
                order_item()
                break
            else:
                complete_order()
                break
        elif food_item == '*':
            if len(order_list) == 0:
                print('\nNothing to remove, basket is empty\n')
                clear_screen()
                print(FORMATTED_MENU)
                print(instructions)
                order_item()
                break
            else:
                remove_item()
            break
        elif food_item.isdigit():
            try:
                food_item = int(food_item) - 1
                order_list.append(MENU[food_item])
                this_item = (MENU[food_item])
                clear_screen()
                print(FORMATTED_MENU)
                print(instructions)
                print(
                    f'You ordered Item {this_item[0]}, {this_item[1]}'
                    f' priced at {this_item[2]}\n')
                food_item = input('What other item would you like? ')
            except IndexError:
                clear_screen()
                print(FORMATTED_MENU)
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
    print(f'You have removed {removed_item[1]} from your order.\n')
    order_list.pop()
    order_item()


def complete_order():
    """
    Function to complete order and arguments to Order class and its functions
    """
    while True:
        order_complete = input(
            "Are you ready to complete your order? (Yes/No). To cancel your order enter 'C'.\n")
        order_complete = order_complete.capitalize()
        if order_complete == 'Yes':
            this_order = Order(name, delivery_type, address,
                               order_list, generate_order_number(SALES_WORKSHEET))
            this_order.print_receipt()                   
            this_order.append_sales()
            break
        elif order_complete == 'No':
            order_item()
            break
        elif order_complete == 'C':
            quit = input(
                'Are you sure you want to cancel the order? (Yes/No)\n')
            quit = quit.capitalize()
            if quit == 'Yes':
                order_list.clear()
                clear_screen()
                thank_you()
                sleep(2)
                clear_screen()
                welcome()
                break
            elif quit == 'No':
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

        if admin_password == PASSWORD:
            clear_screen()
            print(pyfiglet.figlet_format('Access granted!'))
            sleep(2)
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
