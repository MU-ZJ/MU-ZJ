class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit

    def withdrawl(self, withdrawl):
        self.balance -= withdrawl

checking_account = Account("FD332", 100)
checking_account.deposit(50)
print(checking_account.balance)