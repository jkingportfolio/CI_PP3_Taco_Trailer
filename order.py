from google_sheet import *
from datetime import datetime, timedelta
import os
from time import sleep
from tabulate import tabulate


class Order:
    """
    Class that will take an order
    """

    def __init__(self, name, delivery_type, address, order_list, order_number):
        self.name = name
        self.delivery_type = delivery_type
        self.address = address
        self.order_list = order_list
        self.order_number = order_number

    def print_receipt(self):
        """
        Function to print order
        """
        print()
        self.processing_order()
        print('***** Order Receipt *****\n')
        print(f'Order time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        print(f'Order Number: {self.order_number}')
        print(f'Name: {self.name}')
        print(f'Delivery Type: {self.delivery_type.capitalize()}')
        print(f'Address: {self.address}\n')
        print('***** Order Summary *****\n')
        # print('\n'.join(map(str, self.order_list)))
        self.format_order_list()
        print()
        self.total_order_cost()
        self.delivery_time()

    def format_order_list(self):
        print(tabulate(self.order_list, headers=[
            'Item', 'Name', 'Cost (£)'], tablefmt="simple", numalign="center"))

    def append_sales(self):
        """
        Function to add sold items and value to google sheets
        """
        append_order_data = [self.name, self.delivery_type,
                             self.address, str(self.order_list), self.order_cost_output(), self.order_time(), self.order_number]
        worksheet_to_update = SHEET.worksheet('Sales')
        worksheet_to_update.append_row(append_order_data)
        print("worksheet updated successfully\n")
        sleep(2)

    def total_order_cost(self):
        """
        Calculate total order cost as per order list
        """
        order_cost = 0
        delivery_charge = 10

        for item in self.order_list:
            order_cost = order_cost + float(item[-1].replace('£', ''))

        if self.delivery_type == "DELIVERY":
            print(f'The subtotal of your order is £{float(order_cost):.2f}')
            order_cost = order_cost + delivery_charge
            print(
                f'There is a delivery charge of £{float(delivery_charge):.2f}')
            print(
                f'Total cost calculated with delivery £{float(order_cost):.2f}\n')
        else:
            print(f'The total cost of your order is £{float(order_cost):.2f}')
            print('There is no delivery charge\n')
        return order_cost

    def order_cost_output(self):
        order_cost = 0
        delivery_charge = 10

        for item in self.order_list:
            order_cost = order_cost + float(item[-1].replace('£', ''))
        return order_cost


    def processing_order(self):
        """
        Function to clear screen
        """
        print('"Processing order...')
        sleep(2)
        if (os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')

    def delivery_time(self):
        """
        Calculate current time and delivery time
        """
        current_time = datetime.now()
        order_ready_time = current_time + timedelta(minutes=15)
        order_ready_time = order_ready_time.strftime("%Y-%m-%d %H:%M:%S")

        if self.delivery_type == "Delivery":
            print(f'Your order will be delivered at {order_ready_time}\n')
        elif self.delivery_type == "Collection":
            print(
                f'Your order will be ready for collection at {order_ready_time}\n')

    def order_time(self):
        """
        Get order time
        """
        order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return order_time
