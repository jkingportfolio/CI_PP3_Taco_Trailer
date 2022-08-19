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
        print(f'\nYou ordered {order_list}')

    def print_receipt(self):
        """
        Function to print order
        """
        print('passed to print order function succesfully')
        print('***** Order Receipt *****')
        print(name)
        print(delivery_type)
        print(address)
        print(order_list)

    def append_sales(self):
        """
        Function to add sold items and value to google sheets
        """
        worksheet_to_update = SHEET.worksheet('Sales')
        worksheet_to_update.append_row(order)
        print("worksheet updated successfully\n")
