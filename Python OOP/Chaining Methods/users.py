class User:
    def __init__(self, name, email,account_balance):
        self.name = name
        self.email = email
        self.account_balance = account_balance 

    def make_deposit(self, amount):
        self.account_balance += amount
        return self	
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f" Name : {self.name} , account_balance : {self.account_balance}")
        return self
    
    def transfer_money(self,trans):
        u1.account_balance-=trans
        u3.account_balance+=trans
        print(f"u1.account_balance : {u1.account_balance} , u3.account_balance {u3.account_balance}")
        return self


u1=User("Marah","marah@marah.com",200)
u2=User("Dana","dana@dana.com",900)
u3=User("Reem","Reem@Reem.com",70)

# u1.make_deposit(100)
# u1.make_deposit(150)
# u1.make_deposit(400)
# u1.make_withdrawal(200)
# u1.display_user_balance()
# u1.transfer_money(200)
u1.make_deposit(100).make_deposit(150).make_deposit(400).make_withdrawal(200).display_user_balance().transfer_money(200)

# u2.make_deposit(100)
# u2.make_deposit(150)
# u2.make_withdrawal(200)
# u2.make_withdrawal(150)
# u2.display_user_balance()
u2.make_deposit(100).make_deposit(150).make_withdrawal(200).make_withdrawal(150).display_user_balance()



# u3.make_deposit(300)
# u3.make_withdrawal(100)
# u3.make_withdrawal(150)
# u3.make_withdrawal(200)
# u3.display_user_balance()
u3.make_deposit(300).make_withdrawal(100).make_withdrawal(150).make_withdrawal(200).display_user_balance()


