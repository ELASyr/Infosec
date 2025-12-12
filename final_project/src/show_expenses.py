import sqlite3

DB = "final_project/database/expenses.db"

def show_expenses():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = c.fetchall()
    conn.close()

    print("\n=== All Expenses ===")
    for row in rows:
        print(row)

if __name__ == "__main__":
    show_expenses()
