from datetime import datetime
import random


def auth():
    authenticated = False

    account_nums = [125241425, 482815472, 979581414]
    allowed_password = ['passwordDennis', 'passwordKamau', 'passwordMwaura']

    login_regester = int(input("Press 1 to Login\nPress 2 to Register"))

    if login_regester == 1:
        account = int(input('Enter your Account Number\n'))

        if account in account_nums:
            password = input('Enter your password\n')
            user_id = account_nums.index(account)

            if password == allowed_password[user_id]:
                authenticated = True
                print(f'Welcome {account}')
                print(f'Login Successful at {datetime.now()}')
            else:
                print('Password Incorrect, Please try again\n')
        else:
            print('User not found, Please try again\n')

    elif login_regester == 2:

        # Generate account number
        account_num = random.randint(111111111, 999999999)

        print(f"Welcome, your account number is {account_num}\n")

        preffered_password = input('Please set a password\n')

        account_nums.append(account_num)
        allowed_password.append(preffered_password)

        authenticated = True

    else:
        print('Invalid input')

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
    user_authenticated = False

    while True:
        if user_authenticated:
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
        else:
            user_authenticated = auth()


init()
