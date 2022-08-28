"""
Admin functions module
"""
from google_sheet import *
from tabulate import tabulate
from command_line import clear_screen


ORDER_RECORDS = SALES_WORKSHEET.get_all_values()
FORMATTED_ORDERS = (tabulate(ORDER_RECORDS, headers=['Name', 'Order Type', 'Address', 'Items', 'Cost (£)', 'Order Time / Date', 'Order Number'],
                             tablefmt="simple", numalign="center"))


def admin_dashboard():
    clear_screen()
    while True:
        record_count = list(filter(None, SALES_WORKSHEET.col_values(1)))
        total_records = str(len(record_count)+1)
        total_rec_int = int(total_records)
        print('Logged in as Administrator\n\nTo view records enter (1)\nTo view pending orders enter (2)\n')
        admin_option = input('Please select an option: \n')
        clear_screen()
        if admin_option == '1':
            print('Option 1 selected\n')
            while True:
                print(f'There are {total_records} records available')
                record_number = input(
                    'Please enter record number to display or 0 to go back: ')
                clear_screen()
                record_number = int(record_number)
                if record_number < total_rec_int and record_number > 1:
                    try:
                        view_records(record_number)
                    except IndexError:
                        print(f'Record "{record_number}" does not exist, please enter valid record number')
                elif record_number == 0:
                    break
                else:
                    print(
                        f'Record "{record_number}" does not exist, please enter valid record number')
        elif admin_option == '2':
            print('Option 2 selected')
            break
        else:
            print('Thats not an option')
            

# def pending_orders():
    # calculate time now
    # parse times ordered
    # if time now minus time ordered < 15 minutes print order

def view_records(record_number):
    print(f'You are viewing order number: {record_number}')
    record_formatted = ORDER_RECORDS[record_number - 1]
    print('*' * 25)
    print(f'Order Number: {record_formatted[6]}')
    print(f'Order Time: {record_formatted[5]}')
    print(f'Name: {record_formatted[0]}')
    print(f'Order Type: {record_formatted[1]}')
    print(f'Address: {record_formatted[2]}')
    print(f'Items: {record_formatted[3]}')
    print(f'Cost: {record_formatted[4]}')
    print('*' * 25)
