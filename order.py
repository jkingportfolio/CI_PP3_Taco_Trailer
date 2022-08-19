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

    def delivery_type(self, delivery):
        """
        Determine delivery type
        """
        print('Is this order for Delivery or Collection?\n')
        while True:
            delivery_method = input('Please enter delivery or collection: \n')
            delivery_method = delivery_method.upper()
            if delivery_method == 'DELIVERY':
                print()
                print(
                    f'You selected {delivery_method.capitalize()} \
                    for your order.')
                preview_order(order)
                break
            elif delivery_method == 'COLLECTION':
                print()
                print(
                    f'You selected {delivery_method.capitalize()} \
                        for your order.')
                preview_order(order)
                break
            else:
                print()
                print('Please enter a valid input.')
        return delivery_method

    def order_item(self):
        """
        Order function
        """
        food_item = input('What would you like to order? ')

        while True:
            food_item = food_item.upper()
            if food_item == "Q":
                break
            elif food_item == "NO":
                delivery_type()
                # preview_order(order)
                break
            else:
                print(food_item)
                order.append(food_item)
                food_item = input('What other item would you like? ')

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
