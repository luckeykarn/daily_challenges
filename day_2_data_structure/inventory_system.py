inventory = {}

def add_item(item_name, quantity):
    if item_name in inventory:
        print(f"{item_name} already exists in the inventory. Use stock to add more.")
    else:
        inventory[item_name] = quantity
        print(f"{item_name} added to the inventory with quantity {quantity}.")

def restock_item(item_name,quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
        print(f"{item_name} restocked. New quantity: {inventory[item_name]}.")
    else:
        print(f"{item_name} does not exist in the inventory. Use add_item to add it first.")

def sell_item(item_name, quantity):
    if item_name in inventory:
        if inventory[item_name] >= quantity:
            inventory[item_name] -= quantity
            print(f"{quantity} of {item_name} sold. Remaining quantity: {inventory[item_name]}.")
        else:
            print(f"Not enough {item_name} in stock to sell {quantity}. Available: {inventory[item_name]}.")
    else:
        print(f"{item_name} does not exist in the inventory.")

def inventory_print():
    print("Inventory List:")
    for item in sorted(inventory.keys()):
        print(f"- {item}: {inventory[item]}")

while True:
    command = input("\nEnter command (add, restock, sell, print, exit): ").lower()

    if command == "add":
        item = input("Enter item name: ")
        count = int(input("Enter stock count: "))
        add_item(item, count)

    elif command == "restock":
        item = input("Enter item name: ")
        count = int(input("Enter restock count: "))
        restock_item(item, count)

    elif command == "sell":
        item = input("Enter item name: ")
        count = int(input("Enter quantity to sell: "))
        sell_item(item, count)

    elif command == "print":
        inventory_print()

    elif command == "exit":
        print("Exiting Inventory System.")
        break

    else:
        print("Invalid command. Try again.")