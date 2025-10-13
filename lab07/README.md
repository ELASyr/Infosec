 Lab 7 — Crontab in Linux (Python Automation)

This lab demonstrates automating a Python script with **cron** on Linux (WSL).

# Script
`write_time.py` logs a timestamp every minute to `log.txt`.

# Crontab entry
```bash
* * * * * /usr/bin/python3 /home/user_elaman11/Infosec/lab7/write_time.py
