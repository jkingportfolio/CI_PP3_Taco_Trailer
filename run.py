"""
Main python file
"""
import os
import getpass
from admin import *
from google_sheet import *
import pyfiglet
from termcolor import colored
from datetime import datetime, timedelta
from time import sleep
from order import Order


order_list = []
name = None
delivery_type = None
address = None


def welcome():
    """
    Display welcome message and ask for user 
    input to place order or admin access
    """
    clear_screen()
    title = 'Welcome to the Taco Trailer'
    print(pyfiglet.figlet_format(title))
    print('Hello, would you like to place an order?\n')
    while True:
        place_order = input(
            'Please enter a valid input (Y/N). Or for'
            ' Admin Access enter (A).\n')
        place_order = place_order.capitalize()

        if place_order == 'Y':
            clear_screen()
            customer_details()
            break
        elif place_order == 'N':
            clear_screen()
            thank_you()
            break
        elif place_order == 'A':
            admin_access()
            break
        else:
            print(
                colored(f'{place_order} is not a valid input, please try again!', 'yellow'))


def customer_details():
    """
    Collect users name, delivery and address via input
    """
    global name
    global delivery_type
    global address

    print('We would like to take your details.\n')
    while True:
        first_name = input('Please enter your first name: \n')
        if first_name.isalpha():
            break
        else:
            print(colored(
                '\nPlease enter a valid name that does not'
                ' contain numbers or special characters\n', 'yellow'))
    while True:
        surname = input('Please enter your surname: \n')
        if surname.isalpha():
            break
        else:
            print(colored(
                '\nPlease enter a valid name that does not'
                ' contain numbers or special characters\n', 'yellow'))
    name = (f'{first_name} {surname}')
    clear_screen()
    print(pyfiglet.figlet_format(f'Hi {name}!\n'))
    while True:
        delivery_type = input('Please enter your delivery'
                              ' type. Delivery (D) Collection (C): \n')
        delivery_type = delivery_type.capitalize()
        if delivery_type == 'D':
            delivery_type = 'Delivery'
            print()
            print(
                f'You selected {delivery_type.capitalize()} for your order.\n')
            while True:
                address_number = input('Please enter your house number: \n')
                if address_number.isdigit():
                    address_number = int(address_number)
                    break
                else:
                    print(
                        f'"{address_number}" is not a number. Please enter a number')
            while True:
                address_street = input('\nPlease enter your street name: \n')
                if address_street != '' and all(chr.isalpha() or chr.isspace() for chr in address_street):
                    break
                else:
                    print(
                        f'"{address_street}" contains numbers/special character. Please enter a valid input')
            address = (f'{address_number} {address_street}')
            break
        elif delivery_type == 'C':
            delivery_type = 'Collection'
            print()
            print(
                f'You selected {delivery_type.capitalize()} for your order.\n')
            address = 'The Taco Trailer'
            break
        else:
            print()
            print(colored('Please enter a valid input.\n','yellow'))

    clear_screen()
    print('Thank you for your details!\n')
    print('Loading our menu...\n')
    sleep(2)
    clear_screen()
    display_menu()


def display_menu():
    """
    Display the formatted menu
    """
    print(FORMATTED_MENU)
    order_item()


def generate_order_number(worksheet):
    """
    Parse google sheets sales page to find next row, this row is the current order number
    """
    row_list = list(filter(None, worksheet.col_values(1)))
    return str(len(row_list)+1)


def order_item():
    """
    Order function to add/remove items to order list, cancel/complete order 
    """
    instructions = ("\nAdd item by entering item number.\n"
                    "To remove last item enter 'R'.\n"
                    "To cancel order enter 'Q'.\n"
                    "To preview order enter 'P'.\n"
                    "To complete order enter 'X'.\n")

    print(instructions)
    food_item = input("Please enter a valid input: \n")
    while True:
        food_item = food_item.capitalize()
        if food_item == "Q":
            clear_screen()
            quit = input(colored(
                'Are you sure you want to cancel the order? (Y/N)\n', 'yellow'))
            quit = quit.capitalize()
            if quit == 'Y':
                order_list.clear()
                clear_screen()
                thank_you()
                sleep(2)
                clear_screen()
                welcome()
                break
            elif quit == 'N':
                clear_screen()
                print(FORMATTED_MENU)
                order_item()
                break
            else:
                print(colored('Im sorry i need a valid input: ', 'yellow'))
        elif food_item == "X":
            if len(order_list) == 0:
                clear_screen()
                print(FORMATTED_MENU)
                print(colored('\nCannot complete order, basket is empty.', 'yellow'))
                order_item()
                break
            else:
                complete_order()
                break
        elif food_item == 'R':
            if len(order_list) == 0:
                clear_screen()
                print(FORMATTED_MENU)
                print(colored('\nNothing to remove, basket is empty', 'yellow'))
                order_item()
                break
            else:
                remove_item()
            break
        elif food_item == "P":
            clear_screen()            
            print(tabulate(order_list, headers=['Item', 'Name', 'Cost (£)'],
                           tablefmt="simple", numalign="center"))
            close_preview = input(colored(
                '\nRetun to order screen? (Y)\n', 'green'))
            close_preview = close_preview.capitalize()
            if close_preview == 'Y':
                clear_screen()
                print(FORMATTED_MENU)
                order_item()
                break
            else:
                print(colored('Im sorry i need a valid input: ', 'yellow'))
        elif food_item.isdigit() and int(food_item) > 0:
            try:
                food_item = int(food_item) - 1
                order_list.append(MENU[food_item])
                this_item = (MENU[food_item])
                clear_screen()
                print(FORMATTED_MENU)
                print(colored(
                    f'\nYou ordered Item {this_item[0]}, {this_item[1]}'
                    f' priced at {this_item[2]}', 'green'))
                print(instructions)
                food_item = input('What other item would you like? \n')
            except IndexError:
                clear_screen()
                print(FORMATTED_MENU)
                print(colored(
                    f'\nIm sorry Item {food_item + 1} does not exist.'
                    ' Please enter a valid item number', 'yellow'))
                order_item()
                break
        else:
            clear_screen()
            print(FORMATTED_MENU)
            print(colored(
                f'\nIm sorry but {food_item} is not a menu'
                ' option. Please enter a valid input', 'yellow'))
            order_item()
            break


def remove_item():
    """
    Pop last item added to order list
    """
    clear_screen()
    print(FORMATTED_MENU)
    removed_item = order_list[-1]
    print(
        colored(f'\nYou have removed {removed_item[1]} from your order.', 'green'))
    order_list.pop()
    order_item()


def complete_order():
    """
    Function to complete order and pass arguments to Order class and its functions
    """
    order_time = datetime.now() + timedelta(hours=1)
    clear_screen()
    while True:
        order_complete = input(
            "Are you ready to complete your order? (Y/N).\n")
        order_complete = order_complete.capitalize()
        if order_complete == 'Y':
            this_order = Order(name, delivery_type, address,
                               order_list, generate_order_number(SALES_WORKSHEET), order_time)
            this_order.print_receipt()
            this_order.append_sales()
            break
        elif order_complete == 'N':
            clear_screen()
            print(FORMATTED_MENU)
            order_item()
            break
        elif order_complete == 'C':
            quit = input(colored(
                'Are you sure you want to cancel the order? (Y/N)\n', 'yellow'))
            quit = quit.capitalize()
            if quit == 'Y':
                order_list.clear()
                clear_screen()
                thank_you()
                sleep(2)
                clear_screen()
                welcome()
                break
            elif quit == 'N':
                clear_screen()
                print(FORMATTED_MENU)
                order_item()
                break
        else:
            clear_screen()
            print(
                colored(f'Im sorry "{order_complete}" is an invalid input\n', 'yellow'))

    while True:
        finish = input(
            "Please press 'Q' to quit. \n")
        finish = finish.capitalize()
        if finish == 'Q':
            clear_screen()
            thank_you()
            break
        else:
            print('Im sorry that is an invalid input.')


def admin_access():
    """
    Password to access admin dashboard that has access to records and
    ability to edit the menu
    """
    clear_screen()
    password_guesses = 3
    print(f'You have {password_guesses} remaining guesses.\n')
    while True:
        admin_password = getpass.getpass("Please enter Admin Password:\n")

        if admin_password == PASSWORD:
            clear_screen()
            print(pyfiglet.figlet_format('Access granted!'))
            sleep(2)
            admin_dashboard()
            welcome()
            break
        else:
            clear_screen()
            password_guesses -= 1
            if password_guesses > 0:
                print(colored(
                    f'Incorrect password. Remaining password'
                    f' attempts {password_guesses}\n', 'yellow'))
            elif password_guesses == 0:
                print(pyfiglet.figlet_format('Access denied!'))
                sleep(2)
                clear_screen()
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
    Function to display thank you message
    """
    title = 'Thanks for visiting!'
    print(pyfiglet.figlet_format(title))


def main():
    """
    Run all program functions
    """
    welcome()


main()
