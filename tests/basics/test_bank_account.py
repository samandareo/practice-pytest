from projects.basics.bank_account import BankAccount


class TestBankAccount:

    def setup_method(self):
        self.account = BankAccount("Sam", 56548845, 100)

    def test_deposit_with_zero(self):
        result = self.account.deposit(0)
        assert result == "Amount is 0"

    def test_deposit(self):
        result = self.account.deposit(20)
        assert result == "You deposit 20$, Your balance: 120$"

    def test_withdraw_with_greater_than_amount(self):
        result = self.account.withdraw(1000)
        assert result == "Amount is greater than balance"

    def test_withdraw(self):
        result = self.account.withdraw(100)
        assert result == "You withdraw 100$, Your balance: 0"

    def test_show_info(self):
        expected = "Name: Sam\nAccount Number: 56548845\nBalance: 100$"
        assert self.account.show_info() == expected
