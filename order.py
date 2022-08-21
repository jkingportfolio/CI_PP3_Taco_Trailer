from datetime import datetime, timedelta
import os
from time import sleep


class Order:
    """
    Class that will take an order
    """

    def __init__(self, name, delivery_type, address, order_list):
        self.name = name
        self.delivery_type = delivery_type
        self.address = address
        self.order_list = order_list

    def preview_order(self):
        """
        Preview order so far function
        """
        print(f'\nYou ordered {self.order_list}')

    def print_receipt(self):
        """
        Function to print order
        """
        print()
        self.clear_screen()
        print('***** Order Receipt *****\n')
        print(f'Order time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        print(f'Name: {self.name}')
        print(f'Delivery Type: {self.delivery_type.capitalize()}')
        print(f'Address: {self.address}\n')
        print('***** Order Summary *****\n')
        print('\n'.join(map(str, self.order_list)))
        print()
        self.total_order_cost()
        self.delivery_time()

    def append_sales(self):
        """
        Function to add sold items and value to google sheets
        """
        worksheet_to_update = SHEET.worksheet('Sales')
        worksheet_to_update.append_row(order)
        print("worksheet updated successfully\n")

    def total_order_cost(self):
        """
        Calculate total order cost as per order list
        """
        order_cost = 0
        delivery_charge = 10

        for item in self.order_list:
            order_cost = order_cost + float(item[-1].replace('£',''))

        if self.delivery_type == "DELIVERY":
            print(f'The subtotal of your order is £{float(order_cost):.2f}')
            order_cost = order_cost + delivery_charge
            print(f'There is a delivery charge of £{float(delivery_charge):.2f}')
            print(
                f'Total cost calculated with delivery £{float(order_cost):.2f}\n')
        else:
            print(f'The total cost of your order is £{float(order_cost):.2f}')
            print('There is no delivery charge\n')

    def clear_screen(self):
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

        if self.delivery_type == "DELIVERY":
            print(f'Your order will be delivered at {order_ready_time}\n')
        elif self.delivery_type == "COLLECTION":
            print(
                f'Your order will be ready for collection at {order_ready_time}\n')
