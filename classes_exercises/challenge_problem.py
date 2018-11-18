#create a bank account class that has two attributes: Owener, balance
#This class should contain two methods: deposit, withdraw where withdraw <= balance
class Account():

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return "Deposit accepted. Your new balance is: {}".format(self.balance)
    
    def withdraw(self, amount):
        if (self.balance < amount):
            return "You cannot withdraw more than your balance"
        else:
            self.balance = self.balance - amount
            return "You have withdrawn {}. Your new balance is: {}".format(amount, self.balance)
    def __str__(self):
        return f"{self.owner}, your balance is {self.balance}"

acct1 = Account('zac', 100)
print(acct1.__str__())
print(acct1.deposit(150))
print(acct1.withdraw(150))
print(acct1.withdraw(150))