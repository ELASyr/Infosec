import sqlite3

DB = "final_project/database/expenses.db"

def show_stats():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT category, SUM(price) FROM expenses GROUP BY category")
    rows = c.fetchall()
    conn.close()

    print("\n=== Total Spent by Category ===")
    for category, total in rows:
        print(f"{category}: {total} KGS")

if __name__ == "__main__":
    show_stats()
