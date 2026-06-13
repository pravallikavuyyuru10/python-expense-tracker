with open("expenses.txt", "a") as file:
    file.write("Food - 200\n")
    file.write("Travel - 100\n")
    file.write("Shopping - 500\n")

with open("expenses.txt", "r") as file:
    for expense in file:
        print(expense.strip())
