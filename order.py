from datetime import datetime, timedelta
from tabulate import tabulate
from google_sheet import *
from taco_trailer_command_line import load_animation


class Order:
    """
    Class that will create an order instance.
    """

    def __init__(self, _name: str, _delivery_type: str, _address: str,
                 _order_list: list, order_number: str, order_time: str):
        self._name = _name
        self._delivery_type = _delivery_type
        self._address = _address
        self._order_list = _order_list
        self.order_number = order_number
        self.order_time = order_time

    def print_receipt(self):
        """
        Function to print a formatted order receipt to the command line.
        """
        print()
        load_animation('Processing order.')
        print('***** Order Receipt *****\n')
        print(f'Order time: {self.order_time}\n')
        print(f'Order Number: {self.order_number}')
        print(f'Name: {self._name}')
        print(f'Delivery Type: {self._delivery_type.capitalize()}')
        print(f'Address: {self._address}\n')
        print('***** Order Summary *****\n')
        self.format_order_list()
        print()
        self.total_order_cost()
        self.delivery_time()

    def format_order_list(self):
        """
        Function to formats current order list to a table.
        """
        print(tabulate(self._order_list, headers=[
            'Item', 'Name', 'Cost (£)'], tablefmt="simple", numalign="center"))

    def append_sales(self):
        """
        Function to append sold items and value to
        google sheets 'sales' worksheet.
        """
        append_order_data = [self._name, self._delivery_type,
                             self._address, str(self._order_list),
                             self.order_cost_output(),
                             str(self.order_time), self.order_number]
        worksheet_to_update = SHEET.worksheet('Sales')
        worksheet_to_update.append_row(append_order_data)

    def total_order_cost(self):
        """
        Function to calculate total order cost as per current order list.
        """
        order_cost = 0
        delivery_charge = 10

        for item in self._order_list:
            order_cost = order_cost + float(item[-1].replace('£', ''))

        if self._delivery_type == "Delivery":
            print(f'The subtotal of your order is £{float(order_cost):.2f}')
            order_cost = order_cost + delivery_charge
            print(
                f'There is a delivery charge of £{float(delivery_charge):.2f}')
            print(
                f'Total cost calculated with delivery'
                f' £{float(order_cost):.2f}\n')
        else:
            print(f'The total cost of your order is £{float(order_cost):.2f}')
            print('There is no delivery charge\n')

    def order_cost_output(self) -> int:
        """
        Function to output calculate delivery charge value and return
        complete order cost.
        """
        order_cost = 0
        delivery_charge = 10

        for item in self._order_list:
            order_cost = order_cost + float(item[-1].replace('£', ''))

        if self._delivery_type == "Delivery":
            order_cost = order_cost + float(delivery_charge)
            return order_cost
        else:
            return order_cost

    def delivery_time(self):
        """
        function to calculate current time and delivery time.
        """
        current_time = datetime.now()
        order_ready_time = current_time + timedelta(hours=1, minutes=15)
        order_ready_time = order_ready_time.strftime("%H:%M:%S %Y-%m-%d")

        if self._delivery_type == "Delivery":
            print(f'Your order will be delivered at {order_ready_time}\n')
        elif self._delivery_type == "Collection":
            print(
                f'Your order will be ready for collection'
                f' at {order_ready_time}\n')
