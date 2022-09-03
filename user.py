class User:
    """
    Class that will create an order
    """

    def __init__(self, admin_access, user_name, password,
                    first_name, surname, address_number, address_street):
        self.admin_access = admin_access
        self.user_name = user_name
        self.password = password
        self.first_name = first_name
        self.surname = surname
        self.address_number = address_number
        self.address_street = address_street

    def append_user(self):
        """
        Append new user credentials to google sheets users worksheet
        """
        append_order_data = [self.admin_access, self.user_name,
                             self.password, self.first_name, self.surname,
                             self.order_number, self.address_number, self.address_street]
        worksheet_to_update = SHEET.worksheet('Users')
        worksheet_to_update.append_row(append_order_data)