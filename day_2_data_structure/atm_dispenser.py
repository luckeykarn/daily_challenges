
def atm_dispenser(amount):
    if amount <= 0:
        print("Invalid amount.Enter a positive number.")
        return
    if amount % 100 != 0:
        print("Amount must be a multiple of Rs100.")
        return

    print(f"Dispensing Rs{amount} using least number of notes:")

    notes = [2000, 500, 200, 100]
    note_count = {}

    for note in notes:
        count = amount // note
        if count > 0:
            note_count[note] = count
            amount -= note * count

    for note, count in note_count.items():
        print(f"Rs{note} x {count} = Rs{note * count}")

    total_notes = sum(note_count.values())
    print(f"\nTotal notes dispensed:{total_notes}")

try:
    amount = int(input("Enter the amount to withdraw(Rs):"))
    atm_dispenser(amount)
except ValueError:
    print("Please enter a valid number.")
   

