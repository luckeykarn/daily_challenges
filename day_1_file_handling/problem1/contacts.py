import csv
import os

FILENAME = "contacts.csv"

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. List All Contacts")
    print("4. Exit")

    choice = input("Choose an option: ")

    # Add contact
    if choice == '1':
        name = input("Enter a Name: ").lower()
        phone = input("Enter a Phone Number: ")
        email = input("Enter an Email: ")

        with open("contacts.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, email])
            print("Contact added successfully.")

    # Search contact
    elif choice == '2':
        name = input("Enter name to search: ").lower()
        found = False

        if not os.path.exists("contacts.csv"):
            print("No contacts found.")
        else:
            with open("contacts.csv", 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0].lower() == name:
                        print(f"Found: Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
                        found = True
                        break

            if not found:
                print("Contact not found.")

    # List all contacts
    elif choice == '3':
        if not os.path.exists("contacts.csv"):
            print("No contacts found.")
        else:
            with open("contacts.csv", 'r') as file:
                reader = csv.reader(file)
                print("\nContact List:")
                for row in reader:
                    if row:
                        print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")

    # Exit
    elif choice == '4':
        print("Exit Contact Book.")
        break

    else:
        print("Invalid choice. Please try again.")
