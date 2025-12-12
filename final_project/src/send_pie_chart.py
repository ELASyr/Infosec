from telegram import Bot

BOT_TOKEN = "YOUR_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_chart():
    bot = Bot(token=BOT_TOKEN)
    bot.send_photo(chat_id=CHAT_ID, photo=open("final_project/screenshots/chart.png", "rb"))

if __name__ == "__main__":
    send_chart()
