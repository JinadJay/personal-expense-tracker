expenses = []
use = []
date = []

while True:
    amount = int(input("Enter amount: "))
    category = input("Enter category: ")
    time = input("Input Date: ")

    expenses.append(amount)
    use.append(category)
    date.append(time)

    choice = input("Press 1 to add, 2 to exit: ")
    if choice == "2":
        break

for i in range(len(expenses)):
    print(f"amount: {expenses[i]} | category: {use[i]} | time: {date[i]}")