from datetime import datetime, timedelta

"""
Class that will take an order
"""


class Order:
    """
    self
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
        print(f'Order time: {datetime.now()}')
        print('***** Order Receipt *****\n')
        print(f'Name: {self.name}')
        print(f'Delivery Type: {self.delivery_type.capitalize()}')
        print(f'Address: {self.address}\n')
        print('***** Order Summary *****\n')
        print('\n'.join(map(str, self.order_list)))
        print()
        self.total_order_cost()      
        print(f'Your order will be ready at {datetime.now() + timedelta(minutes=10)}\n')

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
            order_cost = order_cost + float(item[-1])

        if self.delivery_type == "DELIVERY":
            print(f'The subtotal of your order is £{float(order_cost)}')
            order_cost = order_cost + delivery_charge
            print(f'There is a delivery charge of £{float(delivery_charge)}')
            print(f'Total cost calculated with delivery £{float(order_cost)}')
        else:            
            print(f'The total cost of your order is £{order_cost}')
            print('There is no delivery charge')
