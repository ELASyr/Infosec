import sqlite3
import matplotlib.pyplot as plt

DB = "final_project/database/expenses.db"

def make_pie_chart():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT category, SUM(price) FROM expenses GROUP BY category")
    rows = c.fetchall()
    conn.close()

    categories = [row[0] for row in rows]
    totals = [row[1] for row in rows]

    plt.figure(figsize=(6, 6))
    plt.pie(totals, labels=categories, autopct="%1.1f%%")
    plt.title("Expenses by Category")
    plt.savefig("final_project/screenshots/chart.png")
    plt.close()

if __name__ == "__main__":
    make_pie_chart()
