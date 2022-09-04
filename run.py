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
from taco_trailer_command_line import clear_screen, load_animation, validate_password, password_criteria
from order import Order
from user import User


order_list = []
name = None
delivery_type = None
address = None


def welcome(message='Hello, would you like to place an order or login?\n'):
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
    print(
        '\nPlease select one of the below options.\n\n[1] - To login\n'
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
            customer_details()
        else:
            clear_screen()
            print(
                '\nPlease select one of the below options.\n\n[1] - To login\n'
                '[2] - To create as account\n[3] - Continue as guest\n')
            print(colored(
                f'Im sorry but {user_login_answer} is an invalid choice, please enter a valid input.\n', 'yellow'))


def login_screen(error_message=''):
    global name
    global delivery_type
    global address
    clear_screen()
    print('\nPlease enter your credentials.')
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
            message = f'Im sorry but {user_name} does not exist.'
            login_screen(message)
            break
    while True:
        password = getpass.getpass('Password: \n')
        if user_name == 'Admin' and password == user_password:
            admin_dashboard()
            welcome()
            break
        elif password == user_password:
            clear_screen()
            print('Passwords match!')
            sleep(2)
            member_address = logins[member_number].get('Address')
            address = member_address
            member_name = logins[member_number].get('Name')
            name = member_name
            print(member_name)
            sleep(2)
            member_delivery_choice()
            break
        else:
            clear_screen()
            print('Incorrect password, please try again.\n')
            print(f'Currently attempting to sign in as {user_name}.\n')


def member_delivery_choice():
    clear_screen()
    global delivery_type
    global address
    while True:
        print(
            'What delivery type would you like?\n\n[D] - Delivery\n[C] - Collection\n[Q] - Quit to main menu\n')
        delivery_choice = input('Please select a valid input: \n').capitalize()
        clear_screen()
        if delivery_choice == 'D':
            print(
                f'This order is for delivery.\n\nWe have your address listed as {address}.\n\nIs this correct?\n[Y] - Yes\n[N] - No')
            accept_delivery = input('').capitalize()
            if accept_delivery == 'Y':
                clear_screen()
                delivery_type = 'Delivery'
                load_animation('Processing delivery details.')
                display_menu()
                break
            elif accept_delivery == 'N':
                print('Please enter delivery details required.\n')
                address_number = input('Please enter house number\n')
                address_street = input('Please enter street name\n')
                address = address_number + '' + address_street
                clear_screen()
                delivery_type = 'Delivery'
                load_animation('Processing delivery details')
                display_menu()
                break
        elif delivery_choice == 'C':
            address = 'The Taco Trailer'
            delivery_type = 'Collection'
            clear_screen()
            load_animation('Processing delivery details')
            display_menu()
            break
        elif delivery_choice == 'Q':
            clear_screen()
            load_animation('Cancelling all user inputs.')
            welcome()
            break
        else:
            clear_screen()
            print(
                f'Im sorry but "{delivery_choice}" in not an option/ Please enter a valid input.\n')


def create_account():
    clear_screen()
    print('\nPlease provide the following details to create an account\n')
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
                    print('Password is valid and matches re entry.\n')
                    break
                elif password != password_validate:
                    clear_screen()
                    print(f'Currently creating password for: {user_name}\n')
                    print(
                        'First password entry meets the password creation criteria.\n')
                    print(
                        'Im sorry those passwords do not match, please try re enter your password again.\n')
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


def members_area():
    print(
        'What would you like to do?\n[1] - Make an order\n[2] - View previous orders\n[3] - Change password')
    while True:
        user_choice = input('User input:\n')
        if user_choice == '1':
            print('Option 1 selected')
        elif user_choice == '2':
            print('Option 2 selected')
        elif user_choice == '3':
            print('Option 3 selected')
        else:
            print('Please enter a valid input.\n')


def customer_details():
    """
    Collect users name, delivery and address via input
    """
    global name
    global delivery_type
    global address

    print('We would like to take your details.\n')
    while True:
        first_name = input('Please enter your first name: \n').strip()
        if first_name.isalpha():
            break
        else:
            print(colored(
                '\nPlease enter a valid name that does not'
                ' contain numbers or special characters\n', 'yellow'))
    while True:
        surname = input('Please enter your surname: \n').strip()
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
                              ' type. Delivery (D) Collection (C): \n').strip()
        delivery_type = delivery_type.capitalize()
        if delivery_type == 'D':
            delivery_type = 'Delivery'
            print()
            print(
                f'You selected {delivery_type.capitalize()} for your order.\n')
            while True:
                address_number = input(
                    'Please enter your house number: \n').strip()
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
            print(colored('Please enter a valid input.\n', 'yellow'))

    clear_screen()
    print('Thank you for your details!\n')
    # print('Loading our menu...\n')
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
    food_item = input("Please enter a valid input: \n").strip()
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
                clear_screen()
                print(tabulate(order_list, headers=['Item', 'Name', 'Cost (£)'],
                               tablefmt="simple", numalign="center"))
                print('')
                print(colored('Im sorry i need a valid input.', 'yellow'))
                sleep(3)

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
    order_time = order_time.strftime("%H:%M:%S %Y-%m-%d")
    clear_screen()
    while True:
        order_complete = input(
            "Are you ready to complete your order? (Y/N).\n").strip()
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
            "Please press 'Q' to quit. \n").strip()
        finish = finish.capitalize()
        if finish == 'Q':
            clear_screen()
            thank_you()
            break
        else:
            print('Im sorry that is an invalid input.')


# def admin_access():
#     """
#     Password to access admin dashboard that has access to records and
#     ability to edit the menu
#     """
#     clear_screen()
#     password_guesses = 3
#     print(
#         colored(f'You have {password_guesses} remaining guesses.\n', 'yellow'))
#     while True:
#         admin_password = getpass.getpass("Please enter Admin Password:\n")

#         if admin_password == PASSWORD:
#             clear_screen()
#             print(pyfiglet.figlet_format('Access granted!'))
#             sleep(2)
#             admin_dashboard()
#             welcome()
#             break
#         else:
#             clear_screen()
#             password_guesses -= 1
#             if password_guesses > 0:
#                 print(colored(
#                     f'Incorrect password. Remaining password'
#                     f' attempts {password_guesses}\n', 'yellow'))
#             elif password_guesses == 0:
#                 print(pyfiglet.figlet_format('Access denied!'))
#                 sleep(2)
#                 clear_screen()
#                 welcome()


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
