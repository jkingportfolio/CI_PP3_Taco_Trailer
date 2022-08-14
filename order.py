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
