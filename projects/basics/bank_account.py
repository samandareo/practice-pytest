class BankAccount:

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"You deposit {amount}$, Your balance: {self._balance}$"
        return f"Amount is 0"

    def withdraw(self, amount):
        if amount <=self._balance:
            self._balance -= amount
            return f"You withdraw {amount}$, Your balance: {self._balance}"
        return "Amount is greater than balance"

    def show_info(self):
        return f"Name: {self.name}\nAccount Number: {self.account_number}\nBalance: {self._balance}$"

john_account = BankAccount("John Doe", 484544688, 100)
print(john_account.deposit(0))
print("------------------------------")
print(john_account.deposit(20))
print("------------------------------")
print(john_account.withdraw(150))
print("------------------------------")
print(john_account.withdraw(120))