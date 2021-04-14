from datetime import datetime


def auth():
    authenticated = False
    name = input('what is your name?\n')

    allowed_users = ['Dennis', 'Kamau', 'Mwaura']
    allowed_password = ['passwordDennis', 'passwordKamau', 'passwordMwaura']

    if name in allowed_users:
        password = input('Enter your password\n')
        user_id = allowed_users.index(name)

        if password == allowed_password[user_id]:
            authenticated = True
            print(f'Welcome {name}')
            print(f'Login Successful at {datetime.now()}')
        else:
            print('Password Incorrect, Please try again\n')
    else:
        print('Name not found, Please try again\n')

    return authenticated


def withdraw():
    withdraw_amount = int(input('How much would you like to withdraw?: '))
    if withdraw_amount > 0:
        print('take your cash\n')
    else:
        print('Withdrawal Amount has to be greater than Zero\n')


def deposit():
    account_balance = 0.00
    deposit_amount = int(input('Enter Amount to deposit?: '))
    if deposit_amount > 0:
        print(f'Current Balance is Ksh {deposit_amount + account_balance}\n')
    else:
        print('Your deposit amount should be greater than Zero\n')


def handle_complaint():
    complaint = input('What issue would you like to report?:\n')
    print('Thank you for contacting us\n')
    # do something with complaint


def init():
    print("Welcome to ZuriATM\n")
    login_regester = input(print("Enter 1 to Login\n2 to register"))


    while auth():
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')
        print('4. Log Out')

        selected_option = int(input('Please select an option: '))

        if selected_option == 1:
            withdraw()
        elif selected_option == 2:
            deposit()
        elif selected_option == 3:
            handle_complaint()
        elif selected_option == 4:
            print('Log out Successful')
            break
        else:
            print('Invalid option selected, Please try again\n')


init()
