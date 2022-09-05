from google_sheet import *

class User:
    """
    Class to create new user instance.
    """

    def __init__(self, user_name, password, admin_access,
                 _name, _address):
        self.user_name = user_name
        self.password = password
        self.admin_access = admin_access
        self._name = _name
        self._address = _address

    def append_user(self):
        """
        Function to append new user credentials to 
        google sheets 'Users' worksheet.
        """
        append_order_data = [self.user_name,
                             self.password,
                             self.admin_access,
                             self._name,
                             self._address]
        worksheet_to_update = SHEET.worksheet('Users')
        worksheet_to_update.append_row(append_order_data)
