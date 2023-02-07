class BankAccount:
    bank_accounts = []

    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
       

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if (self.balance < amount):
            print(
                f"Insufficient funds: Available balance: {self.balance}. Requested amount: {amount}")
        else:
            self.balance = self.balance - amount
        return self

    def display_account_info(self):
        print(f"Interest rate: {self.int_rate}")
        print(f"Available balance: {self.balance}")
        return self

    def yield_interest(self):
        if (self.balance > 0):
            self.balance = self.balance + (self.balance * self.int_rate)
        return self

    @classmethod
    def print_instances(cls):
        for i in range(0, len(cls.bank_accounts)):
            print(cls.bank_accounts[i].balance)
            print(cls.bank_accounts[i].int_rate)


Account1 = BankAccount(0.25, 50)
Account2 = BankAccount(0.25, 50)

Account1.deposit(25).deposit(55).deposit(45).withdraw(
    1).yield_interest().display_account_info()
Account2.deposit(150).deposit(200).withdraw(20).withdraw(25).withdraw(
    3).withdraw(40).yield_interest().display_account_info()

print(BankAccount.print_instances())
