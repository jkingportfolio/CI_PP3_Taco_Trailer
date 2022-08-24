"""
Admin functions module
"""

def admin_dashboard():
    while True:
        admin_option = input('Please select an option: ')
        if admin_option == '1':
            print('Option 1 selected')
        elif admin_option == '2':
            print('Option 2 selected')
        else:
            print('Thats not an option')
        break