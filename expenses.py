#!/usr/bin/env python3
import sqlite3
import sys
from datetime import datetime, timedelta
import os
import requests

DB_NAME = "expenses.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT,
        price REAL,
        date TEXT
    )
    """)
    conn.commit()
    conn.close()
    print("Database initialized.")

def add_expense(item, price, date):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses(item, price, date) VALUES (?, ?, ?)", (item, price, date))
    conn.commit()
    conn.close()
    print("Expense added.")

def list_expenses():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        print(row)

def calculate_total():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(price) FROM expenses")
    total = cursor.fetchone()[0]
    conn.close()
    print("Total spent:", total)

def weekly_report():
    today = datetime.today()
    week_ago = today - timedelta(days=7)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT item, price, date FROM expenses WHERE date BETWEEN ? AND ?", 
                   (week_ago.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d")))
    rows = cursor.fetchall()
    conn.close()

    total = sum(r[1] for r in rows)
    report = "📅 Weekly Expense Report\n"
    for r in rows:
        report += f"{r[0]} - {r[1]} som ({r[2]})\n"
    report += f"\nTotal: {total} som"

    print(report)
    send_telegram(report)

def send_telegram(message):
    token = os.getenv("EXP_TELEGRAM_TOKEN")
    chat_id = os.getenv("EXP_TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("Telegram token or chat ID not set.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data={"chat_id": chat_id, "text": message})
    print("Telegram message sent.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: init | add | list | total | report")
    elif sys.argv[1] == "init":
        init_db()
    elif sys.argv[1] == "add":
        add_expense(sys.argv[2], float(sys.argv[3]), sys.argv[4])
    elif sys.argv[1] == "list":
        list_expenses()
    elif sys.argv[1] == "total":
        calculate_total()
    elif sys.argv[1] == "report":
        weekly_report()
