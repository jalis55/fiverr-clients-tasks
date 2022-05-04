from mimetypes import init


class BankAccount:
    def __init__(self,account_number,name,balance) -> None:
        self.account_number=account_number
        self.name=name
        self.balance=balance
    
    def deposite(self,amount):
        self.balance +=amount

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -=amount

    def bankfee(self):
        self.balance=(95/100)*self.balance
    def display(self):
        print(f"Account no {self.account_number}")
        print(f"Name:{self.name}")
        print(f"Balance:{self.balance}")

jalis=BankAccount(1122112,'Jalis Mahamud Tarif',50000)

jalis.display()