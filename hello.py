"""Simple personal expense tracker in python"""
import os

# Custom Exception for handling invalid expenses


class InvalidExpenseError(Exception):
    """Exception raised for errors in the input expense amount."""
    pass

# Expense class using Object-Oriented Programming


class Expense:
    """
    Represents an expense with a category, amount, and description.

    Attributes:
        category (str): The category of the expense (e.g., Food, Transport).
        amount (float): The amount of money spent.
        description (str): A brief description of the expense.
    """

    def __init__(self, category, amount, description):
        if amount < 0:
            raise InvalidExpenseError("Expense amount cannot be negative.")
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"{self.category}: ${self.amount:.2f} - {self.description}"

# ExpenseTracker class to manage the collection of expenses


class ExpenseTracker:
    """
    Tracks a list of expenses and provides methods to add, view, and summarize expenses.

    Attributes:
        expenses (list): A list to store all the expense objects.
    """

    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        """Adds a new expense to the tracker."""
        self.expenses.append(expense)

    def view_expenses(self):
        """Displays all recorded expenses."""
        os.system('clear')
        if not self.expenses:
            print("No expenses found.")
        else:
            print("All Expenses:")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. {expense}")

    def summarize_expenses(self):
        """Prints a summary of expenses by category and the total amount spent."""
        os.system('clear')
        if not self.expenses:
            print("No expenses found.")
        else:
            total_expenses = sum(expense.amount for expense in self.expenses)
            print(f"Total expenses: ${total_expenses:.2f}")

            print("\nExpenses by Category:")
            category_summary = {}
            for expense in self.expenses:
                category_summary[expense.category] = category_summary.get(
                    expense.category, 0) + expense.amount

            for category, total in category_summary.items():
                print(f"{category}: ${total:.2f}")


class MenuManager:
    """
    A context manager to handle the setup and teardown of the user interface.

    Ensures the terminal is cleared at the start and prints a goodbye message on exit.
    """

    def __enter__(self):
        os.system('clear')
        print("Welcome to the SPETa | Simple Personal Expenses Tracker")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Goodbye!")


def print_menu():
    """Print the menu options"""
    print("\n\nPlease select an option from the menu below:")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Summarize expenses")
    print("q. Quit")


def get_non_empty_input(prompt):
    """Get non-empty input from the user."""
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Input cannot be empty.")


def get_valid_amount(prompt):
    """Get a valid numeric amount from the user."""
    while True:
        user_input = input(prompt).strip()
        if user_input.replace('.', '', 1).isdigit():
            return float(user_input)
        print("Invalid amount. Please enter a numeric value.")


def add_expense(tracker):
    """Prompts the user to enter a new expense and adds it to the tracker."""
    try:
        category = get_non_empty_input("Enter the expense category: ").strip()
        amount = get_valid_amount("Enter the expense amount: ")
        description = get_non_empty_input(
            "Enter the expense description: ").strip()

        expense = Expense(category, amount, description)
        tracker.add_expense(expense)
        print("Expense added successfully.")
    except InvalidExpenseError as e:
        print(f"Error: {e}")


def mainloop(tracker):
    """Main loop of the program"""
    while True:
        print_menu()
        choice = input("Enter your choice (1-3 or 'q' to quit): ")

        if choice == "1":
            add_expense(tracker)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.summarize_expenses()
        elif choice == "q":
            confirm = input("Are you sure you want to quit? (y/n): ")
            if confirm.lower() == 'y':
                break
        else:
            print("Invalid choice. Please try again.")


# Using context manager and classes
with MenuManager():
    my_expense_tracker = ExpenseTracker()
    mainloop(my_expense_tracker)
