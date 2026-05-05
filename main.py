from bank_account import BankAccount 
from person import Person
from utils import *

def main():
    people = []  

    while True:
        # Display menu
        print("Choose an option:")
        print("1. Add a new person")
        print("2. Add an account to a person")
        print("3. Show all balances")
        print("4. Quit")

        choice = input().strip()

        # Option 1: Add a new person
        if choice == "1":
            new_person = person_data()
            people.append(new_person)

        # Option 2: Add an account to an existing person
        elif choice == "2":
            name = input("Enter the person's name:\n")
            found = None
            for person in people:
                if person.name == name:
                    found = person
                    break
            if found:
                account_number = int(input("Enter a 4-digit account number:\n"))
                balance = float(input("Enter the initial balance:\n"))
                new_account = BankAccount(account_number, balance)
                found.add_account(new_account)
            else:
                print("Person not found.")

        # Option 3: Show all balances
        elif choice == "3":
            if not people:
                print("No data to show.")
            else:
                balance_summary(people)

        # Option 4: Quit
        elif choice == "4":
            print("Goodbye!")
            break

        # Invalid input
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()

