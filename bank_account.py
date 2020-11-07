
class Bank_Account:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${amount}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Amount Withdrawn: ${amount}")
        if amount > self.balance:
            print("Insufficient funds.")
            self.balance -= 10
    
    def get_balance(self):
        print(self.balance)

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def print_receipt(self):
        stars = []
        # account_num = self.account_number
        # len_list_account = list(len(str(account_num)))
        # account_num_str_list = list(str(account_num))
        # for i in len_list_account:
        #     if i < len(len_list_account) - 4:
        #         stars += "*"
        #     elif i == len(len_list_account) - 4:
        #         stars += account_num_str_list[i]
        #     elif i == len(len_list_account) - 3:
        #         stars += account_num_str_list[i]
        #     elif i == len(len_list_account) - 2:
        #         stars += account_num_str_list[i]
        #     elif i == len(len_list_account) - 1:
        #         stars += account_num_str_list[i]

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

logan_account = Bank_Account("Logan Reynolds", 1234567890, 875634175796, 197643.45)

logan_account.withdraw(500)
logan_account.deposit(1000000)
logan_account.print_receipt()