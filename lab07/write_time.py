#!/usr/bin/env python3
import os
from datetime import datetime

# Build a log path inside your lab folder
home_dir = os.path.expanduser("~")
log_path = os.path.join(home_dir, "Infosec", "lab7", "log.txt")

with open(log_path, "a") as f:
    f.write(f"[{datetime.now()}] Cron executed successfully.\n")
