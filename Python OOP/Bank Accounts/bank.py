class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        return self
        
    def withdraw(self, amount):
        if self.balance<amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        else:
            self.balance-=amount
        return self
        
    def display_account_info(self):
        print(f"Balance : {self.balance}")
        return self
        
    def yield_interest(self):
        self.balance=self.balance+(self.balance*self.int_rate)
        return self

account1=BankAccount(0.03,2000)
account2=BankAccount(0.02,50)

account1.deposit(100).deposit(300).deposit(250).withdraw(200).yield_interest().display_account_info()

account2.deposit(100).deposit(300).withdraw(100).withdraw(200).withdraw(40).withdraw(250).yield_interest().display_account_info()


