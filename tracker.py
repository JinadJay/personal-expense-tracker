expenses = []
use = []

while True:
    amount = int(input("Enter amount: "))
    category = input("Enter category: ")

    expenses.append(amount)
    use.append(category)

    choice = input("Press 1 to add, 2 to exit: ")
    if choice == "2":
        break

for i in range(len(expenses)):
    print(f"amount: {expenses[i]} | Category: {use[i]}")