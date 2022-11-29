class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        return self
        
    def withdraw(self, amount):
        if self.balance< amount:
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

class User:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02 , balance=0)
    
    def display_user_info(self):
        print(f"{self.name} +{self.account.display_account_info()}")
        return self
    
    def transfer_money(self,trans,user2):
        self.account.balance-=trans
        user2.account.balance-=trans
        print(f" {self.name} transfered {trans}$  to {user2.name}")
        return self

marah = User("marah","marah@gmail.com")
dana = User("dana","dana@gmail.com")


marah.account.deposit(100)
marah.display_user_info()
dana.account.deposit(300)
dana.display_user_info()
dana.transfer_money(100,marah)
marah.account.deposit(100).withdraw(80).display_account_info()