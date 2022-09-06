"""
Admin functions module
"""
from google_sheet import *
from taco_trailer_command_line import load_animation
from tabulate import tabulate
from taco_trailer_command_line import clear_screen
from datetime import datetime, timedelta
from time import sleep
from termcolor import colored


def admin_dashboard():
    """
    Function to display admin dashboard and accept user input
    from the range of admin options.
    """
    clear_screen()
    record_count = list(filter(None, SALES_WORKSHEET.col_values(1)))
    total_records = str(len(record_count)+1)
    total_rec_int = int(total_records)
    print(colored('Logged in as Administrator\n', 'green'))
    while True:
        print(
            'Please enter a valid input\n\n[1] View records\n[2]'
            ' View pending orders\n[Q] Exit admin dashboard\n')
        admin_option = input('Please select an option: \n').strip()
        clear_screen()
        if admin_option == '1':
            search_records(total_rec_int)
        elif admin_option == '2':
            pending_orders(total_rec_int)
            break
        elif admin_option.capitalize() == 'Q':
            clear_screen()
            load_animation('Logging out as Admin.')
            break
        else:
            print(colored('Logged in as Administrator\n', 'green'))
            print(
                colored(f'Im sorry "{admin_option}" is not'
                        ' a valid option.\n', 'yellow'))


def pending_orders(total_rec_int):
    """
    Function to return pending orders that current time 
    is less than delivered time and display in formatted table
    @param total_rec_int(int): Total number of orders as per 
    google sheet data.
    """
    clear_screen()
    while True:
        current_time = datetime.now()
        local_time = current_time + timedelta(hours=1)
        local_time = local_time.strftime("%H:%M:%S %Y-%m-%d")
        print(f'The current time and date is: {local_time}\n')
        pending_order_time = current_time + timedelta(minutes=45)
        pending_order_time = pending_order_time.strftime("%H:%M:%S %Y-%m-%d")
        FORMATTED_SALES = ORDER_RECORDS

        try:
            for item in FORMATTED_SALES:
                for key in ('Items', 'Address', 'Name'):
                    del item[key]
        except KeyError:
            pass

        pending_order_list = list(
            filter(lambda x: x['Order Time/Date'] >
                   pending_order_time, FORMATTED_SALES))
        if len(pending_order_list) > 0:
            print(tabulate(pending_order_list, headers='keys',
                           tablefmt="simple", numalign="center"))
        else:
            print(colored('There are currently no pending orders!', 'yellow'))
        while True:
            exit = input(
                colored('\nPress "Q" to return to Admin dashboard.\n', 'green'))
            if exit.capitalize() == 'Q':
                admin_dashboard()
                break
            else:
                clear_screen()
                print(f'The current time and date is: {local_time}\n')

                print(tabulate(pending_order_list, headers='keys',
                               tablefmt="simple", numalign="center"))
                print(
                    colored(f'\nIm sorry "{exit}" is not'
                            ' a valid input.', 'yellow'))


def search_records(total_rec_int):
    """
    Function to retreive sales records from google sheets 
    and display them in the CLI via user input of record number.
    @param total_rec_int(int): Total number of orders as per 
    google sheet data.
    """
    while True:
        try:
            print(f'There are {total_rec_int - 1} records available\n')
            print(
                'Please note there is no record for order 1 as this'
                ' is the database header\n')
            record_number = input(colored(
                'Please enter record number to display or "0" to return'
                ' to the Admin dashboard.\n', 'green')).strip()
            clear_screen()
            record_number = int(record_number)
            if record_number < total_rec_int and record_number > 1:
                try:
                    view_records(record_number)
                except IndexError:
                    print(colored(
                        f'Record "{record_number}" does not exist, please'
                        ' enter valid record number', 'yellow'))
            elif record_number == 0:
                break
            else:
                print(colored(
                    f'Record "{record_number}" does not exist, please enter'
                    ' valid record number:\n', 'yellow'))
        except ValueError:
            print(
                colored(f'"{record_number}" is an invalid entry please'
                        ' try again.\n', 'yellow'))


def view_records(record_number):
    """
    Function to return formatted record based on based arguement of record 
    number.
    @param record_number(int): Record number to view as enter by user input.
    """
    print(colored(f'You are viewing order number: {record_number}\n', 'green'))
    record_formatted = ORDER_RECORD_VALUES[record_number - 1]
    print('*' * 25)
    print(f'Order Number: {record_formatted[6]}')
    print(f'Order Time: {record_formatted[5]}')
    print(f'Name: {record_formatted[0]}')
    print(f'Order Type: {record_formatted[1]}')
    print(f'Address: {record_formatted[2]}')
    print('Ordered Items:')
    try:
        record_formatted[3] = record_formatted[3].strip('[]').split('], [')
        for i in range(0, len(record_formatted[3])):
            record_formatted[3][i] = record_formatted[3][i].replace("'", "")
            print(f'- Item Number: {record_formatted[3][i]}')
    except AttributeError:
        for i in range(0, len(record_formatted[3])):
            print(f'- Item Number: {record_formatted[3][i]}')
    print(f'Total order cost: {record_formatted[4]}')
    print('*' * 25 + '\n')
