class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def withdraw(self):
        amount = int(input("how much money do you want ?"))
        if amount <= self.balance:
            print("the money is coming")

    def get_balance(self):
        return self.balance

class SavingAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance, interest_rate):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):


class ChackingAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance, interest_rate, overdraft):
        super().__init__(account_number, owner_name, balance)
        self.overdraft = overdraft


    def withdraw(self):
        if overdraft
