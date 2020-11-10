import random
class Bank_Account:
    routing_number = 927485027
    def __init__(self, full_name, balance):
        self.account_number = ""
        for i in range(8):
            self.account_number += str(random.randrange(0, 9))
        self.account_number = int(self.account_number)
        self.full_name = full_name
        self.balance = balance

    # Calculate the amount deposited Added to the balance and prints out the amount you deposited
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${amount}")

    # Subtract the amount withdrawn from the balance checks if funds are sufficient does the proper calculations if they are not subtracting $10 also this prints out the amount withdrawn
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Amount Withdrawn: ${amount}")
        if amount > self.balance:
            print("Insufficient funds.")
            self.balance -= 10
    
    # Prince out the balance
    def get_balance(self):
        print(f"Balance: ${self.balance}")

    # Adds interest to the account balance
    def add_interest(self):
        balance = self.balance
        interest = balance * 0.00083
        self.balance = self.balance + interest

    # Prints receipt of your account
    def print_receipt(self):
        stars = []

        for i in str(self.account_number):
            stars.append("*")
        str_account_num = str(self.account_number)
        stars[len(stars)-1] = str_account_num[len(stars)-1]
        stars[len(stars)-2] = str_account_num[len(stars)-2]
        stars[len(stars)-3] = str_account_num[len(stars)-3]
        stars[len(stars)-4] = str_account_num[len(stars)-4]

        str_stars = ""
        str_stars = str_stars.join(stars)
        print(f"""
            {self.full_name}
            Account No.: {str_stars}
            Routing No.: {self.routing_number}
            Balance: {self.balance}
        """)

# new account created
logan_account = Bank_Account("Logan R.", 197643.45)
logan_account.withdraw(500)
logan_account.deposit(1000000)
logan_account.print_receipt()

# new account created
Joi_account = Bank_Account("Joi The Awesome", 13799752578995)
Joi_account.get_balance()
Joi_account.add_interest()
Joi_account.print_receipt()

# new account created to test
test_account = Bank_Account("Joi The Awesome", 857799795)
test_account.get_balance()
test_account.add_interest()
test_account.deposit(1000000)
test_account.print_receipt()