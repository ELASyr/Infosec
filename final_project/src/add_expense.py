import sqlite3
from datetime import datetime

DB = "final_project/database/expenses.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            price REAL NOT NULL,
            date TEXT NOT NULL,
            category TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_expense():
    item = input("Item name: ")
    price = float(input("Price: "))
    date = input("Date (YYYY-MM-DD) or leave blank for today: ")
    category = input("Category: ")

    if date.strip() == "":
        date = datetime.today().strftime("%Y-%m-%d")

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(
        "INSERT INTO expenses (item, price, date, category) VALUES (?, ?, ?, ?)",
        (item, price, date, category)
    )
    conn.commit()
    conn.close()
    print("Expense added successfully!")

if __name__ == "__main__":
    init_db()
    add_expense()
