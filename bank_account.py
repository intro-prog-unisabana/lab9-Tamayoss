# bank_account.py
class BankAccount:  
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance                      
    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance:.2f}"    
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount


