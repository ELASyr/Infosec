Personal Expenses Reports Helper

Made by: Nurbolot Pirdinov
Course: Information Security — Final Project

This project is a personal expense-tracking utility designed for the AUCA Information Security course.
It includes a terminal-based expense manager and a Telegram bot that sends automated weekly reports.
All data is stored locally in a secure SQLite database.

Features
1. Terminal Interface

Add expenses (category, amount, note, date)

Smart date parsing (yesterday, 2 days ago, etc.)

View all saved expenses

View statistics:

Today / Yesterday

Totals by category

Last 7 days

Generate pie chart of expenses

Trigger Telegram weekly report manually

2. Telegram Bot

Commands supported:

/start
/add <amount> <category> <note> <date?>
/today
/week
/stats
/chart

3. Automated Weekly Report

A cron task sends the weekly report to the user's Telegram account every Sunday.

4. Secure Local Database

SQLite database (expenses.db)

Protected with parameterized SQL queries

Tokens stored safely in .env

Directory Layout
personal_expenses/
│
├── database/
│   └── expenses.db
│
├── src/
│   ├── add_expense.py
│   ├── show_expenses.py
│   ├── stats.py
│   ├── pie_chart.py
│   ├── send_weekly_report.py
│   ├── menu.py
│   └── bot.py
│
└── README.md

🔗 Video Demonstration

You can watch the full implementation and usage of the Personal Expenses Tracker here:

**https://youtu.be/tAw09zd34m4**

[![Watch the video](https://img.youtube.com/vi/tAw09zd34m4/0.jpg)](https://youtu.be/tAw09zd34m4)

The video shows:

CLI usage

Adding expenses

Viewing stats

Generating pie chart

Telegram bot commands

Automatic weekly report

Cron job demonstration

Security Notes

Secrets stored in .env (never in code)

SQL injection prevented via parameterized queries

Bot restricted to owner’s chat ID

Local database only (no cloud exposure)

Conclusion

This project fulfills all requirements of the AUCA Information Security final assignment.
It demonstrates secure programming, automation with cron, Telegram bot integration, and practical Linux skills.
The system is modular, extendable, and useful for real-world personal expense tracking.
