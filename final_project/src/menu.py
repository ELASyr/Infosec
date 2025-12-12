from add_expense import add_expense
from show_expenses import show_expenses
from stats import show_stats
from pie_chart import make_pie_chart

def menu():
    while True:
        print("\n=== Personal Expenses CLI ===")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Show stats")
        print("4. Generate pie chart")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_stats()
        elif choice == "4":
            make_pie_chart()
        elif choice == "5":
            break

if __name__ == "__main__":
    menu()
