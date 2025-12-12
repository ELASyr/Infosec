# Personal Expenses Reports Helper

Made by: Elaman Abdulloev

Course: Information Security — Final Project

This project is a personal expense-tracking utility designed for the AUCA Information Security course.
It includes a terminal-based expense manager and a Telegram bot that sends automated weekly reports.
All data is stored locally in a secure SQLite database.

## Features
### 1. Terminal Interface

Add expenses (category, amount, note, date)

Smart date parsing (yesterday, 2 days ago, etc.)

View all saved expenses

View statistics:

Today / Yesterday totals

Totals by category

Last 7 days summary

Generate pie chart of expenses

Manually trigger Telegram weekly report
### 2. Telegram Bot

Commands supported:

/start
/add <amount> <category> <note> <date?>
/today
/week
/stats
/chart

### 3. Automated Weekly Report

A cron task sends the weekly report to the user's Telegram account every Sunday.

### 4. Secure Local Database

SQLite database (expenses.db)

Protected with parameterized SQL queries

Tokens stored safely in .env
## Telegram Bot Access

Scan the QR code below to open the Telegram bot:

![Telegram Bot QR Code](final_project/screenshots/telegram_qr.png)

Or open directly:
https://t.me/@elaman_personalexpenses_bot

## Directory Layout

```text
final_project/
├── database/
│   └── expenses.db
│
├── screenshots/
│   ├── add_expense.png
│   ├── stats.png
│   ├── chart.png
│   ├── cron.png
│   └── telegram.png
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

## 🔗 Video Demonstration

You can watch the full implementation and usage of the Personal Expenses Tracker here:

**https://youtu.be/tAw09zd34m4**

[![Watch the video](https://img.youtube.com/vi/tAw09zd34m4/0.jpg)](https://youtu.be/tAw09zd34m4)

## The video shows:

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

## Conclusion

This project fulfills all requirements of the Information Security final assignment.
It demonstrates secure programming, automation with cron, Telegram bot integration, and practical Linux skills.
The system is modular, extendable, and useful for real-world personal expense tracking.
