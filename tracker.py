import csv
import os

all_expenses = []

if os.path.exists("tracker.csv"):
    with open("tracker.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["amount"] = int(row["amount"])
            all_expenses.append(row)
    print("Welcome Back")
else:
    print("no previous data found.")

while True:
    try:
        amount = int(input("Enter amount: "))
    except ValueError:
        print("put in a number.")
        continue

    category = input("Enter category: ")

    expense_item = {"amount": amount, "category": category}

    all_expenses.append(expense_item)

    choice = input("Press 1 to add, 2 to exit: ")
    if choice == "2":
        
        with open("tracker.csv", "w", newline="") as file:
            fieldnames = ["amount", "category"]
            writer = csv.DictWriter(file, fieldnames=["amount", "category"])
            writer.writeheader()
            writer.writerows(all_expenses)
        print("Saved")
        break
            
for item in all_expenses:
    print(f"{item['amount']} was spent on {item['category']}")