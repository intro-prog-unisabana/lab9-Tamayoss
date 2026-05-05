# utils.py
from bank_account import *
from person import *
def person_data():
    name=input("Enter the person's name:\n")
    my_person=Person(name)
    while True:
        account_number=int(input("Enter a 4-digit account number:\n"))
        balance=input("Enter the initial balance:\n")
        my_bank_a= BankAccount(account_number, balance)
        my_person.add_account(my_bank_a)
        entrada=input("Are you done adding accounts? (yes/no):")
        if entrada == "yes":
            break
    return my_person    
def balance_summary(person_list: list):
    for person in person_list:
        total_balance = sum(account.balance for account in person.accounts)
        print(f"{person.name} : {total_balance:.2f}")
