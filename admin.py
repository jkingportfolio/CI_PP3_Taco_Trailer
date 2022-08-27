"""
Admin functions module
"""
from google_sheet import *
from tabulate import tabulate


ORDER_RECORDS = SALES_WORKSHEET.get_all_values()
FORMATTED_ORDERS = (tabulate(ORDER_RECORDS, headers=['Name', 'Order Type', 'Address', 'Items', 'Cost (£)', 'Order Time / Date', 'Order Number'],
                           tablefmt="simple", numalign="center"))

def admin_dashboard():
    while True:
        record_count = list(filter(None, SALES_WORKSHEET.col_values(1)))
        total_records = str(len(record_count)+1)
        admin_option = input('Please select an option: \n')
        if admin_option == '1':
            print('Option 1 selected')
            print(f'There are {total_records} records available')
            record_number = input('Please enter record number to display')
            record_number = int(record_number)
            view_records(record_number)
            # break
        elif admin_option == '2':
            print('Option 2 selected')
            break
        else:
            print('Thats not an option')


# def sales_info():

# def pending_orders():
    # calculate time now
    # parse times ordered
    # if time now minus time ordered < 15 minutes print order

def view_records(record_number):
    print(f'You are viewing order number: {record_number}')
    record_formatted = ORDER_RECORDS[record_number - 1]
    print(f'Name: {record_formatted[0]}')
    print(f'Order Type: {record_formatted[1]}')
    print(f'Address: {record_formatted[2]}')
    print(f'Items: {record_formatted[3]}')
    print(f'Cost: {record_formatted[4]}')
    print(f'Order Time: {record_formatted[5]}')
    print(f'Order Number: {record_formatted[6]}')
    # find last row
    # record numbers = last row number (Record: 1 of {last_row})
    # ask user how many records to show
    # show records
    # plus and minus buttons to go to next and back

# def update_menu():
    #
