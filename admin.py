"""
Admin functions module
"""
from google_sheet import *
from tabulate import tabulate
from command_line import clear_screen
from datetime import datetime, timedelta
from time import sleep
from termcolor import colored


def admin_dashboard():
    clear_screen()
    while True:
        record_count = list(filter(None, SALES_WORKSHEET.col_values(1)))
        total_records = str(len(record_count)+1)
        total_rec_int = int(total_records)
        print('Logged in as Administrator\n\nPlease enter a valid input\n(1) View records\n(2) View pending orders\n')
        admin_option = input('Please select an option: \n')
        clear_screen()
        if admin_option == '1':
            search_records(total_rec_int)
        elif admin_option == '2':
            pending_orders(total_rec_int)
            break
        else:
            print('Thats not an option')


def pending_orders(total_rec_int):
    clear_screen()
    while True:
        current_time = datetime.now()
        local_time = current_time + timedelta(hours=1)
        local_time = local_time.strftime("%H:%M:%S %Y-%m-%d")
        print(f'The current time and date is: {local_time}\n')
        FORMATTED_SALES = ORDER_RECORDS

        for item in FORMATTED_SALES:
            for key in ('Items', 'Address', 'Name'):
                del item[key]

        print(tabulate(FORMATTED_SALES, headers='keys',
                       tablefmt="simple", numalign="center"))

        test_hold = input('\nPress 0 to go back\n')
        if test_hold == '0':
            admin_dashboard()
            break


def search_records(total_rec_int):
    while True:
        try:
            print(f'There are {total_rec_int - 1} records available\nPlease note there is no record for order 1 as this is the database header')
            record_number = input(
                'Please enter record number to display or 0 to go back:\n')
            clear_screen()
            record_number = int(record_number)
            if record_number < total_rec_int and record_number > 1:
                try:
                    view_records(record_number)
                except IndexError:
                    print(colored(
                        f'Record "{record_number}" does not exist, please enter valid record number','yellow'))
            elif record_number == 0:
                break
            else:
                print(colored(
                    f'Record "{record_number}" does not exist, please enter valid record number.\n','yellow'))
        except ValueError:
            print(
                colored(f'"{record_number}" is an invalid entry please try again.\n', 'yellow'))


def view_records(record_number):
    print(f'You are viewing order number: {record_number}\n')
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
    print('*' * 25 +'\n')
