"""
Main python file
"""
import getpass
from admin import admin_dashboard
from google_sheet import *
import pyfiglet
from termcolor import colored
from datetime import datetime, timedelta
from time import sleep
from taco_trailer_command_line import (clear_screen, load_animation,
                                       validate_password, password_criteria)
from order import Order
from user import User


order_list = []
name = None
delivery_type = None
address = None


def welcome(message=colored('Hello, would you like to place an order or login?\n', 'green')):
    """
    Display welcome message and ask for user
    input to place order or admin access
    """
    clear_screen()
    title = 'Welcome to the Taco Trailer'
    print(pyfiglet.figlet_format(title))
    print(message)
    while True:
        place_order = input(
            'Please enter a valid input\n[Y] - Yes\n[N] - No\n').strip()
        place_order = place_order.capitalize()

        if place_order == 'Y':
            clear_screen()
            user_login()
            break
        elif place_order == 'N':
            clear_screen()
            thank_you()
            break
        else:
            welcome(
                colored(f'{place_order} is not a valid input, please try again!\n', 'yellow'))
            break


def user_login():
    print(colored(
        '\nPlease select one of the below options.\n', 'green'))
    print('[1] - To login\n'
          '[2] - To create as account\n[3] - Continue as guest\n')
    while True:
        user_login_answer = input('User input: \n')
        if user_login_answer == '1':
            login_screen()
            break
        elif user_login_answer == '2':
            create_account()
            break
        elif user_login_answer == '3':
            clear_screen()
            customer_details()
            break
        else:
            clear_screen()
            print(colored(
                '\nPlease select one of the below options.\n', 'green'))
            print('[1] - To login\n'
                  '[2] - To create as account\n[3] - Continue as guest\n')
            print(colored(
                f'Im sorry but "{user_login_answer}" is an invalid choice, please enter a valid input.\n', 'yellow'))


def login_screen(error_message=''):
    global name
    global delivery_type
    global address
    clear_screen()
    print(colored('Please enter your credentials.', 'green'))
    print(error_message)
    logins = LOGINS
    users = user_name_list()
    while True:
        user_name = input('Username: \n')
        if user_name.capitalize() == 'Admin':
            member_number = (
                next((i for i, x in enumerate(logins) if x["User Name"] == user_name), None))
            user_password = logins[member_number].get('Password')
            break
        elif user_name in users:
            member_number = (
                next((i for i, x in enumerate(logins) if x["User Name"] == user_name), None))
            user_password = logins[member_number].get('Password')
            break
        else:
            clear_screen()
            message = (
                colored(f'\nIm sorry but "{user_name}" does not exist.\n', 'yellow'))
            login_screen(message)
            break
    password_guesses = 3
    while True:
        password = getpass.getpass('Password: \n')
        if user_name == 'Admin' and password == user_password:
            admin_dashboard()
            welcome()
            break
        elif password == user_password:
            clear_screen()
            load_animation(f'Credentials valid.\n\nLogging in as {user_name}.')
            member_address = logins[member_number].get('Address')
            address = member_address
            member_name = logins[member_number].get('Name')
            name = member_name
            members_area(member_name, member_number)
            break
        else:
            clear_screen()
            password_guesses -= 1
            if password_guesses > 0:
                print(colored(
                    f'Incorrect password. Remaining password'
                    f' attempts {password_guesses}\n', 'yellow'))
                print(f'Currently attempting to sign in as: {user_name}\n')
            elif password_guesses == 0:
                print(pyfiglet.figlet_format('Access denied!'))
                sleep(2)
                clear_screen()
                welcome()


def member_delivery_choice(member_name):
    clear_screen()
    global delivery_type
    global address
    while True:
        print(colored(
            'What delivery type would you like?\n', 'green'))
        print(
            '[D] - Delivery\n[C] - Collection\n[Q] - Quit to main menu\n')
        delivery_choice = input('Please select a valid input: \n').capitalize()
        clear_screen()
        if delivery_choice == 'D':
            print(
                f'This order is for delivery.\n')
            print(colored(f'We have your address listed as {address}.\n','yellow'))
            accept_delivery = input('Is this correct?\n[Y] - Yes\n[N] - No\n').capitalize()
            if accept_delivery == 'Y':
                clear_screen()
                delivery_type = 'Delivery'
                load_animation('Loading menu.')
                display_menu()
                break
            elif accept_delivery == 'N':
                clear_screen()
                print(colored('Please enter delivery details required.\n', 'green'))
                address_number = input('Please enter house number\n')
                address_street = input('Please enter street name\n')
                address = address_number + '' + address_street
                clear_screen()
                delivery_type = 'Delivery'
                load_animation('Loading menu.')
                display_menu()
                break
        elif delivery_choice == 'C':
            address = 'The Taco Trailer'
            delivery_type = 'Collection'
            clear_screen()
            load_animation('Loading menu.')
            display_menu()
            break
        elif delivery_choice == 'Q':
            clear_screen()
            load_animation('Cancelling all user inputs.')
            welcome()
            break
        else:
            clear_screen()
            print(colored(
                f'Im sorry but "{delivery_choice}" in not an option/ Please enter a valid input.\n', 'yellow'))


def create_account():
    clear_screen()
    print(colored('\nPlease provide the following details to create an account\n','green'))
    admin_access = '0'
    while True:
        user_name = input('Please enter a user name: \n')
        if validate_new_username(user_name):
            break

    while True:
        print(password_criteria)
        password = getpass.getpass('Please enter your password: \n')
        if validate_password(password):
            while True:
                password_validate = getpass.getpass(
                    'Please re enter your password:\n')
                if password == password_validate:
                    clear_screen()
                    print(colored('Password is valid and matches re entry.\n','green'))
                    break
                elif password != password_validate:
                    clear_screen()
                    print(colored(f'Currently creating password for: {user_name}\n','green'))
                    print(colored(
                        'First password entry meets the password creation criteria.\n','green'))
                    print(colored(
                        'Im sorry those passwords do not match, please try re enter your password again.\n','yellow'))
            break
        else:
            clear_screen()
            print(f'Currently entered username: {user_name}\n')
            validate_password(password)
    first_name = input('Please enter your first name: \n').strip()
    surname = input('Please enter your surname: \n').strip()
    name = first_name + '' + surname
    address_number = input(
        'Please enter your house number: \n').strip()
    address_street = input('\nPlease enter your street name: \n')
    address = address_number + '' + address_street
    clear_screen()
    load_animation('Thank you for your details. Creating account.')
    new_user = User(user_name, password, admin_access,
                    name, address)
    new_user.append_user()
    members_area()


def members_area(member_name, member_number):
    print(pyfiglet.figlet_format(f'Hi {member_name}'))
    print(
        'What would you like to do?\n[1] - Make an order\n[2] - View previous orders\n[3] - Change password\n')
    while True:
        user_choice = input('User input:\n')
        if user_choice == '1':
            member_delivery_choice(member_name)
            break
        elif user_choice == '2':
            print('Option 2 selected')
        elif user_choice == '3':
            change_password(member_number)
        else:
            print('Please enter a valid input.\n')


def customer_details():
    """
    Collect users name, delivery and address via input
    """
    global name
    global delivery_type
    global address

    print(colored('We would like to take your details.\n','green'))
    while True:
        first_name = input('Please enter your first name: \n').strip()
        if first_name.isalpha():
            break
        else:
            clear_screen()
            print(colored(
                'Please enter a valid name that does not'
                ' contain numbers or special characters\n', 'yellow'))
    while True:
        surname = input('Please enter your surname: \n').strip()
        if surname.isalpha():
            break
        else:
            clear_screen()
            print(colored(
                'Please enter a valid surname that does not'
                ' contain numbers or special characters\n', 'yellow'))
    name = (f'{first_name} {surname}')
    clear_screen()
    print(pyfiglet.figlet_format(f'Hi {name}'))
    while True:
        print(colored('Please enter your delivery type.\n','green'))
        delivery_type = input('Delivery (D) Collection (C): \n').strip()
        delivery_type = delivery_type.capitalize()
        if delivery_type == 'D':
            delivery_type = 'Delivery'
            clear_screen()
            print(colored(
                f'\nYou selected {delivery_type.capitalize()} for your order.\n','green'))
            while True:
                address_number = input(
                    'Please enter your house number: \n').strip()
                if address_number.isdigit():
                    address_number = int(address_number)
                    break
                else:
                    clear_screen()
                    print(colored(
                        f'Invalid entry "{address_number}" is not a number. Please enter a number.\n','yellow'))
            while True:
                address_street = input('\nPlease enter your street name: \n')
                if address_street != '' and all(chr.isalpha() or chr.isspace() for chr in address_street):
                    break
                else:
                    clear_screen()
                    print(colored(
                        f'Invalid entry "{address_street}" contains numbers/special character. Please enter a valid input.','yellow'))
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
            clear_screen()
            print(pyfiglet.figlet_format(f'Hi {name}'))            
            print(colored(f'Im sorry but "{delivery_type}" is not a valid option. Please enter a valid input.\n', 'yellow'))

    clear_screen()
    print(colored('Thank you for your details!','green'))
    sleep(2)
    load_animation('Loading menu.')
    clear_screen()
    display_menu()


def display_menu():
    """
    Display the formatted menu
    """
    print(FORMATTED_MENU)
    order_item()


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
    food_item = input(
        colored("Please enter a valid input: \n", 'green')).strip()
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
                clear_screen()
                print(tabulate(order_list, headers=['Item', 'Name', 'Cost (£)'],
                               tablefmt="simple", numalign="center"))
                print('')
                print(colored('Im sorry i need a valid input.', 'yellow'))
                sleep(2)
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
                food_item = input(
                    colored('What other item would you like? \n', 'green'))
            except IndexError:
                clear_screen()
                print(FORMATTED_MENU)
                print(colored(
                    f'\nIm sorry Item "{food_item + 1}" does not exist.'
                    ' Please enter a valid item number', 'yellow'))
                order_item()
                break
        else:
            clear_screen()
            print(FORMATTED_MENU)
            print(colored(
                f'\nIm sorry but "{food_item}" is not a menu'
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
    order_time = order_time.strftime("%H:%M:%S %Y-%m-%d")
    clear_screen()
    while True:
        order_complete = input(colored("Are you ready to complete your order? (Y/N).\n",'green')).strip()
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
        finish = input(colored(
            "Please press 'Q' to quit. \n", 'green')).strip()
        finish = finish.capitalize()
        if finish == 'Q':
            clear_screen()
            thank_you()
            break
        else:
            print('Im sorry that is an invalid input.')


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


if __name__ == "__main__":
    main()
