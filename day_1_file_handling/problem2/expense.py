import csv
from datetime import datetime

FILENAME = "expenses.csv"

while True:
    print("\n---Expense Tracker ---")
    print("1. Add Expense")
    print("2.Today's All Expenses")
    print("3. Show All Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Expense
    if choice == '1':
        description = input("Enter expense description: ")
        amount = input("Enter amount: ")
        date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

        if not date:
            date = datetime.today().strftime("%Y-%m-%d")

        with open( "expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([description, amount, date])

        print("Expense added successfully!")

    # Add Today's Expense
    elif choice == '2':
        total = 0
        today = datetime.today().strftime("%Y-%m-%d")
        try:
            with open( "expenses.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[2] == today:
                        total += float(row[1])
            print(f"Today's Total Expense: Rs{total:.2f}")
        except FileNotFoundError:
            print("No expenses found yet.")

    # Add Weekly Expenses
    elif choice == '3':
        try:
            with open( "expenses.csv", "r") as file:
                reader = csv.reader(file)
                print("\n--- Weekly Expenses ---")
                for row in reader:
                    print(f"Description: {row[0]}, Amount: Rs{row[1]}, Date: {row[2]}")
        except FileNotFoundError:
            print("No expenses found yet.")

    # Step 4: Exit
    elif choice == '4':
        print("Exit")
        break

    else:
        print("Invalid choice. Please try again.")
