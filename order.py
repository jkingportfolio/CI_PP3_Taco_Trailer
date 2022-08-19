"""
Class that will take an order
"""


class Order:
    """
    self
    """

    def __init__(self, name, delivery, items_ordered, total_cost):
        self.name = name
        self.delivery = delivery
        self.items_ordered = items_ordered
        self.total_cost = total_cost



    def preview_order(self, order):
        """
        Preview order so far function
        """
        print(f'\nYou ordered {order}')
        while True:
            order_more = input('Would you like to add to your order? ')
            if order_more == 'Yes':
                order_item()
                break
            elif order_more == 'No':
                print_order(order)
                break
            else:
                print('That is not a valid input')

    def print_order(self, order):
        """
        Function to print order
        """
        print('passed to print order function succesfully')
        print(order)
        append_sales(order)

    def append_sales(self, order):
        """
        Function to add sold items and value to google sheets
        """
        worksheet_to_update = SHEET.worksheet('Sales')
        worksheet_to_update.append_row(order)
        print("worksheet updated successfully\n")
