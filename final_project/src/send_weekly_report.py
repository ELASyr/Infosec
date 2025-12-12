import sqlite3
from telegram import Bot

BOT_TOKEN = "YOUR_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
DB = "final_project/database/expenses.db"

def send_report():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT date, item, price, category FROM expenses ORDER BY date DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()

    text = "📊 Weekly Expense Report\n\n"
    for row in rows:
        text += f"{row[0]} — {row[1]} — {row[2]} KGS — {row[3]}\n"

    bot = Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=text)

if __name__ == "__main__":
    send_report()
