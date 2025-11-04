class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        print(f"{amount} som qoshildi. Yangi balans: {self.balance}")
    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"{amount} som yechildi. Qolgan balans: {self.balance}")
        else:
            print("Balans yetarli emas")
account1=BankAccount("Miyasar", 1000)
account1.deposit(500) 
account1.withdraw(200) 
account1.withdraw(2000)