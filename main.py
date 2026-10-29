from bankaccount import BankAccount

#create bank account
user_name = input("Welcome to the Bank! Please enter your name: ")

#generate bank account starting info
account_info = BankAccount(user_name)

#Display opening menu
menu_choice = int(input("Please choose an option: \n1. Make a deposit \n2. Make a withdrawal \n3. View account information \n4. Quit"))


while menu_choice != 4:
    if menu_choice == 1:
        make_deposit()
#1. Make a deposit
#2. Make a Withdraw
#3. See account balance
#4. Quit

