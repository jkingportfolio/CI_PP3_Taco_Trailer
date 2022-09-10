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
from user import User, validate_name, validate_address


_order_list = []
_name = None
_delivery_type = None
_address = None
logins = LOGINS


def welcome(message=''):
    """
    Function to display welcome message and accept user
    input to continue, log in or quit.
    """
    clear_screen()
    title = 'Welcome to the Taco Trailer'
    print(pyfiglet.figlet_format(title))
    print(colored('Hello, would you like to place an order or'
                  ' login?\n', 'green'))
    while True:
        print('[Y] - Yes\n[N] - No')
        print(f'\n{message}')
        place_order = input(
            'Please enter a valid input:\n').strip()
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
                colored(f'Im sorry but "{place_order}" is not a valid input,'
                        'please enter a valid input.\n', 'yellow'))
            break


def user_login():
    """
    Function to accept user input to login, create account, continue
    as guest or quit to main menu.
    """
    prompt = (colored(
        '\nPlease select one of the below options.\n', 'green'))
    options = ('[1] - To login\n'
               '[2] - To create as account\n'
               '[3] - Continue as guest\n'
               '[Q] - To return to main menu\n')
    print(prompt)
    print(options)
    while True:
        user_login_answer = input('Please enter a valid input: \n')
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
        elif user_login_answer.capitalize() == 'Q':
            quit_to_main()
            break
        else:
            clear_screen()
            print(prompt)
            print(options)
            print(colored(
                f'Im sorry but "{user_login_answer}" is not a valid choice,'
                ' please enter a valid input.\n', 'yellow'))


def login_screen(error_message=''):
    """
    Function to accept user input of user name and
    password then validate with google sheet data.
    @param error_message(string): Error message dependant on error that occurs
    """
    global _name
    global _delivery_type
    users = user_name_list()
    clear_screen()
    while True:
        print(colored('Please enter your username. Or enter "Q" to quit.', 'green'))
        print(error_message)
        user_name = input('Username: \n')
        if user_name in users:
            member_number = (
                next((i for i, x in enumerate(logins)
                      if x["User Name"] == user_name), None))
            user_password = logins[member_number].get('Password')
            password_check(user_name, member_number, user_password)
            break
        elif user_name.capitalize() == 'Q':
            quit_to_main()
            break
        else:
            clear_screen()
            message = (
                colored(f'\nIm sorry but "{user_name}"'
                        ' does not exist.\n', 'yellow'))
            login_screen(message)
            break


def password_check(user_name, member_number, user_password):
    """
    Function to Validate usernames password is correct
    """
    global _address
    password_guesses = 3
    pass_prompt = (
        colored('Please enter your password. Or enter "Q" to quit.\n', 'green'))
    clear_screen()
    while True:
        print(pass_prompt)
        password = getpass.getpass('Password: \n')
        if user_name == 'Admin' and password == user_password:
            admin_dashboard()
            welcome()
            break
        elif password == user_password:
            load_animation(
                f'Entered credentials are valid.\n\n'
                f'Logging in as {user_name}.')
            member_address = logins[member_number].get('Address')
            _address = member_address
            member_name = logins[member_number].get('Name')
            _name = member_name
            members_area(_name, member_number, user_name)
            break
        elif password.capitalize() == 'Q':
            quit_to_main()
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
                break


def member_delivery_choice(member_name: str, member_number, user_name):
    """
    Function to take user input on current members delivery
    choice.
    """
    clear_screen()
    global _delivery_type
    global _address
    prompt = (colored(
        'Please enter your delivery type.\n', 'green'))
    options = (
        '[D] - Delivery\n[C] - Collection\n[Q] - Quit to main menu\n')
    print(prompt)
    print(options)
    while True:
        delivery_choice = input('Please select a valid input: \n').strip()
        delivery_choice = delivery_choice.capitalize()
        clear_screen()
        if delivery_choice == 'D':
            print('This order is for delivery.\n')
            print(
                colored(f'We have your address listed as'
                        f' "{_address}".\n', 'green'))
            while True:
                accept_delivery = input(
                    'Is this correct?\n[Y] - Yes\n[N] - No\n[Q] - Quit to main menu\n').capitalize()
                if accept_delivery == 'Y':
                    clear_screen()
                    _delivery_type = 'Delivery'
                    print(colored(
                        f'You selected {_delivery_type.capitalize()} for your'
                        ' order.\n', 'green'))
                    sleep(3)
                    load_animation('Loading menu.')
                    display_menu()
                    break
                elif accept_delivery == 'N':
                    clear_screen()
                    print(colored('Please enter delivery details'
                                  ' required.\n', 'green'))
                    _address = validate_address()
                    clear_screen()
                    _delivery_type = 'Delivery'
                    load_animation('Loading menu.')
                    display_menu()
                    break
                elif accept_delivery == 'Q':
                    quit_to_main('log out and quit', member_name,
                                 member_number, user_name)
                    break
                else:
                    clear_screen()
                    print('This order is for delivery.\n')
                    print(colored(f'We have your address listed as'
                                  f' "{_address}".\n', 'green'))
                    print(colored(
                        f'Im sorry but "{accept_delivery}" is not a'
                        ' valid input.\n', 'yellow'))
            break
        elif delivery_choice == 'C':
            _address = 'The Taco Trailer'
            _delivery_type = 'Collection'
            clear_screen()
            print(colored(
                f'You selected {_delivery_type.capitalize()} for your'
                ' order.\n', 'green'))
            sleep(3)
            load_animation('Loading menu.')
            display_menu()
            break
        elif delivery_choice == 'Q':
            quit_to_main('log out and quit', member_name,
                         member_number, user_name)
            break
        else:
            clear_screen()
            print(prompt)
            print(options)
            print(colored(
                f'Im sorry but "{delivery_choice}" in not an option.'
                ' Please enter a valid input.\n', 'yellow'))


def create_account():
    """
    Function to accept all required user inputs to create an account
    and append that data to google sheet.
    """
    clear_screen()
    print(colored('\nPlease provide the following details to'
                  ' create an account\n', 'green'))
    while True:
        user_name = input(
            'Please enter a user name. Otherwise enter [Q] to quit.\n')
        if user_name.capitalize() == 'Q':
            quit_to_main()
            break
        elif validate_new_username(user_name):
            while True:
                print(password_criteria)
                password = getpass.getpass(
                    'Please enter your password. Otherwise enter [Q] to quit. \n')
                if password.capitalize() == 'Q':
                    clear_screen()
                    quit_to_main()
                    break
                else:
                    clear_screen()
                    if validate_password(password):
                        while True:
                            password_validate = getpass.getpass(colored(
                                'Please re enter your password. Otherwise enter [Q] to quit:\n', 'green'))
                            if password_validate.capitalize() == 'Q':
                                clear_screen()
                                quit_to_main()
                                break
                            elif password == password_validate:
                                clear_screen()
                                print(colored('Password is valid and matches'
                                              ' re entry.\n', 'green'))
                                validate_password(password)
                                _name = validate_name()
                                clear_screen()
                                _address = validate_address()
                                clear_screen()
                                load_animation(
                                    'Thank you for your details. Creating account.')
                                print(
                                    colored(f'New user account for "{user_name}" has'
                                            ' been created.', 'green'))
                                print(colored(
                                    '\nPlease note account log in will only be valid upon'
                                    ' program restart.', 'yellow'))
                                new_user = User(user_name, password,
                                                _name, _address)
                                new_user.append_user()
                                user_login()
                                break
                            elif password != password_validate:
                                clear_screen()
                                print(
                                    f'Currently creating password for: {user_name}\n')
                                print(colored(
                                    'First password entry meets the password'
                                    ' creation criteria.\n', 'green'))
                                print(colored(
                                    'Im sorry those passwords do not match, please try'
                                    ' re enter your password again.\n', 'yellow'))
                            else:
                                clear_screen()
                                print(
                                    f'Currently entered username: {user_name}\n')
                        break
            break


def members_area(member_name, member_number, user_name):
    """
    Function to accept user input to make an order, change
    password, or log out as current member.
    @param member_name(string): Members full name taken from
    google sheets 'Users' worksheet.
    @param member_number(string): Members id number taken from
    google sheets 'Users' worksheet.
    @param user_name(string): Members user name taken from
    google sheets 'Users' worksheet.
    """
    print(pyfiglet.figlet_format(f'Hi {member_name}'))
    member_area_instructions = (colored('What would you'
                                        ' like to do?', 'green')) + \
        '\n\n[1] - Make an order\n[2] - Change password\n[Q] - Log out\n'
    print(member_area_instructions)
    while True:
        user_choice = input('Please enter a valid input:\n')
        if user_choice == '1':
            clear_screen()
            member_delivery_choice(member_name, member_number, user_name)
            break
        elif user_choice == '2':
            clear_screen()
            change_password(member_number)
            members_area(member_name, member_number, user_name)
            break
        elif user_choice.capitalize() == 'Q':
            quit_to_main('log out and quit', member_name,
                         member_number, user_name)
            break
        else:
            clear_screen()
            print(pyfiglet.figlet_format(f'Hi {member_name}'))
            print(member_area_instructions)
            print(colored(
                f'Im sorry but "{user_choice}" is not a valid input.'
                ' Please enter a valid input.\n', 'yellow'))


def customer_details():
    """
    Function to accept user input for all required data
    related to customer details.
    """
    global _name
    global _delivery_type
    global _address

    print(colored('We would like to take your details.\n', 'green'))
    _name = validate_name()
    clear_screen()
    print(pyfiglet.figlet_format(f'Hi {_name}'))
    prompt = (colored('Please enter your delivery type.\n', 'green'))
    options = ('[D] - Delivery\n[C] - Collection\n[Q] - Quit to main menu\n')
    print(prompt)
    print(options)
    while True:
        delivery_choice = input('Please enter a valid input: \n').strip()
        delivery_choice = delivery_choice.capitalize()
        if delivery_choice == 'Q':
            quit_to_main()
            break
        elif delivery_choice == 'D':
            _delivery_type = 'Delivery'
            clear_screen()
            print(colored(
                f'\nYou selected {_delivery_type.capitalize()}'
                ' for your order.\n', 'green'))
            _address = validate_address()
            clear_screen()
            print(colored('Thank you for your details!', 'green'))
            sleep(3)
            load_animation('Loading menu.')
            clear_screen()
            display_menu()
            break
        elif delivery_choice == 'C':
            _delivery_type = 'Collection'
            clear_screen()
            print(colored(
                f'You selected {_delivery_type.capitalize()}'
                ' for your order.\n', 'green'))
            sleep(3)
            _address = 'The Taco Trailer'
            clear_screen()
            print(colored('Thank you for your details!', 'green'))
            sleep(3)
            load_animation('Loading menu.')
            clear_screen()
            display_menu()
            break
        else:
            clear_screen()
            print(pyfiglet.figlet_format(f'Hi {_name}'))
            print(prompt)
            print(options)
            print(colored(
                f'Im sorry but "{_delivery_type}" is not a valid option.'
                ' Please enter a valid input.\n', 'yellow'))


def display_menu():
    """
    Function to display the menu formatted by tabulate
    and call the order_item function.
    """
    print(FORMATTED_MENU)
    order_item()


def order_item():
    """
    Function to add/remove items to/from order list, cancel/complete order,
    preview current order and cancel order.
    """
    instructions = ("\nAdd item by entering item number.\n"
                    "To remove last item enter 'R'.\n"
                    "To cancel order and quit enter 'Q'.\n"
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
                'Are you sure you want to cancel the order and quit?'
                ' (Y/N)\n', 'yellow'))
            quit = quit.capitalize()
            if quit == 'Y':
                _order_list.clear()
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
            if len(_order_list) == 0:
                clear_screen()
                print(FORMATTED_MENU)
                print(colored('\nCannot complete order,'
                              ' basket is empty.', 'yellow'))
                order_item()
                break
            else:
                complete_order()
                break
        elif food_item == 'R':
            if len(_order_list) == 0:
                clear_screen()
                print(FORMATTED_MENU)
                print(colored('\nNothing to remove, basket'
                              ' is empty', 'yellow'))
                order_item()
                break
            else:
                remove_item()
            break
        elif food_item == "P":
            clear_screen()
            print(colored('Order Preview\n', 'green'))
            print(tabulate(_order_list, headers=['Item', 'Name', 'Cost (£)'],
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
                print(tabulate(_order_list,
                               headers=['Item', 'Name', 'Cost (£)'],
                               tablefmt="simple", numalign="center"))
                print('')
                print(colored('Please enter "Y" to return to order screen.', 'yellow'))
                sleep(2)
        elif food_item.isdigit() and int(food_item) > 0:
            try:
                food_item = int(food_item) - 1
                _order_list.append(MENU[food_item])
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
    Function to pop the last item from the order list.
    """
    clear_screen()
    print(FORMATTED_MENU)
    removed_item = _order_list[-1]
    print(
        colored(f'\nYou have removed {removed_item[1]}'
                ' from your order.', 'green'))
    _order_list.pop()
    order_item()


def complete_order():
    """
    Function to complete order and pass arguments to
    Order class and its functions.
    """
    order_time = datetime.now() + timedelta(hours=1)
    order_time = order_time.strftime("%H:%M:%S %Y-%m-%d")
    clear_screen()
    while True:
        order_complete = input(
            colored('Are you ready to complete your order?'
                    ' (Y/N).\n', 'green')).strip()
        order_complete = order_complete.capitalize()
        if order_complete == 'Y':
            this_order = Order(_name, _delivery_type, _address,
                               _order_list,
                               generate_order_number(SALES_WORKSHEET),
                               order_time)
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
                'Are you sure you want to cancel the order?'
                ' (Y/N)\n', 'yellow'))
            quit = quit.capitalize()
            if quit == 'Y':
                _order_list.clear()
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
                colored(f'Im sorry "{order_complete}" is an'
                        ' invalid input\n', 'yellow'))

    while True:
        finish = input(colored(
            "Please press 'Q' to quit. \n", 'green')).strip()
        finish = finish.capitalize()
        if finish == 'Q':
            clear_screen()
            thank_you()
            break
        else:
            print(f'Im sorry but {finish} is an invalid input.')


def thank_you():
    """
    Function to display thank you message
    """
    title = 'Thanks for visiting!'
    print(pyfiglet.figlet_format(title))


def quit_to_main(message='quit', member_name='', member_number=None, user_name=''):
    """
    Function to quit to main menu
    """
    clear_screen()
    print(
        colored(f'Are you sure you want to {message} to the main screen?', 'green'))
    print('\n[Y] - Yes\n[N] - No\n')
    while True:
        confirm_quit = input('Please enter a valid input: \n').strip()
        if confirm_quit.capitalize() == 'Y' and user_name == '':
            clear_screen()
            welcome()
            break
        elif confirm_quit.capitalize() == 'Y':
            load_animation(f'Logging {user_name} out.')
            clear_screen()
            welcome()
            break
        elif confirm_quit.capitalize() == 'N' and user_name == '':
            clear_screen()
            welcome()
            break
        elif confirm_quit.capitalize() == 'N':
            clear_screen()
            members_area(member_name, member_number, user_name)
            welcome()
            break
        else:
            clear_screen()
            print(colored('Are you sure you want to quit to the main screen?', 'green'))
            print('\n[Y] - Yes\n[N] - No')
            print(colored(f'\nIm sorry but "{confirm_quit} is not a valid option. Please'
                          ' enter a valid input.\n', 'yellow'))


def main():
    """
    Function to begin script.
    """
    welcome()


if __name__ == "__main__":
    main()
