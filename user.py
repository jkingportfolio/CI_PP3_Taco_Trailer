from google_sheet import *

class User:
    """
    Class that will create an order
    """

    def __init__(self, user_name, password, admin_access,
                 name, address):
        self.user_name = user_name
        self.password = password
        self.admin_access = admin_access
        self.name = name
        self.address = address

    def append_user(self):
        """
        Append new user credentials to google sheets users worksheet
        """
        append_order_data = [self.user_name,
                             self.password,
                             self.admin_access,
                             self.name,
                             self.address]
        worksheet_to_update = SHEET.worksheet('Users')
        worksheet_to_update.append_row(append_order_data)
