"""Simple personal expense tracker in python"""
import os

def print_menu():
    """Print the menu options"""
    print("\n\n-------------------------------------------------")
    print("Please select an option from the menu below:")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Summarize expenses")
    print("q. Quit")


def mainloop():
    """Main loop of the program"""
    while True:
        print_menu()
        choice = input("Enter your choice (1-3 or 'q' to quit): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summarize_expenses()
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def add_expense():
    """Add a new expense to the list"""
    os.system('clear')
    expense_category = input("Enter the expense category: ")
    
    while True:
        try:
            expense_amount = float(input("Enter the expense amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    expense_description = input("Enter the expense description: ")
    expenses.append({
        "category": expense_category,
        "amount": expense_amount,
        "description": expense_description
    })
    print("Expense added successfully.")


def view_expenses():
    """View all expenses"""
    os.system('clear')
    if not expenses:
        print("No expenses found.")
    else:
        print("All Expenses:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense['category']}: ${expense['amount']:.2f} - {expense['description']}")


def summarize_expenses():
    """Summarize all expenses by category"""
    os.system('clear')
    if not expenses:
        print("No expenses found.")
    else:
        total_expenses = sum(expense["amount"] for expense in expenses)
        print(f"Total expenses: ${total_expenses:.2f}")
        
        print("\nExpenses by category:")
        category_summary = {}
        for expense in expenses:
            category_summary[expense["category"]] = category_summary.get(expense["category"], 0) + expense["amount"]
        
        for category, total in category_summary.items():
            print(f"{category}: ${total:.2f}")


expenses = []
os.system('clear')
print("Welcome to the SPETa | Simple Personal Expenses Tracker\n\n")
mainloop()
