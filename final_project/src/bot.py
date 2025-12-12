import os
import sqlite3
import matplotlib.pyplot as plt
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

DB_PATH = os.path.join(os.path.dirname(__file__), "../database/expenses.db")
TOKEN = "8385316367:AAHXHjXfYTbH2qISEMSnpLpNQ7oIuNnz6M0"


def add_expense_to_db(item, price, date, category):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (item, price, date, category) VALUES (?, ?, ?, ?)",
        (item, price, date, category)
    )
    conn.commit()
    conn.close()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to Personal Expense Bot\n\n"
        "Commands:\n"
        "/add item price date category\n"
        "/show - show all expenses\n"
        "/stats - show statistics\n"
        "/chart - pie chart of categories\n"
    )


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        item = context.args[0]
        price = float(context.args[1])
        date = context.args[2]
        category = context.args[3]

        add_expense_to_db(item, price, date, category)
        await update.message.reply_text("Expense added successfully.")
    except Exception:
        await update.message.reply_text("Usage: /add item price date category")


async def show(update: Update, context: ContextTypes.DEFAULT_TYPE):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT item, price, date, category FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        await update.message.reply_text("No expenses yet.")
        return

    msg = "Your expenses:\n\n"
    for r in rows:
        msg += f"{r[0]} - {r[1]} - {r[2]} - {r[3]}\n"

    await update.message.reply_text(msg)


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(price) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    conn.close()

    msg = "Expense statistics:\n\n"
    total = 0
    for cat, val in rows:
        msg += f"{cat}: {val}\n"
        total += val

    msg += f"\nTotal spent: {total}"

    await update.message.reply_text(msg)


async def chart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(price) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    conn.close()

    categories = [r[0] for r in rows]
    values = [r[1] for r in rows]

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=categories, autopct="%1.1f%%")
    plt.title("Expense categories")

    chart_path = "/tmp/chart.png"
    plt.savefig(chart_path)
    plt.close()

    await update.message.reply_photo(photo=open(chart_path, "rb"))


async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("show", show))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("chart", chart))

    await app.run_polling()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
