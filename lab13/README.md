# Lab13 — Keylogging (Educational & Local Only)

**PS:** This lab is for educational purposes on machines you own or with explicit permission. Never use keylogging to spy on others. 

## Files
- `main.py` — safe demo keylogger (logs locally for SESSION_SECONDS)
- `analyze.py` — reads collected logs and shows top tokens
- `simulated_upload.py` — moves rotated logs to `sent/` (local simulation)

## How to run
1. Create a virtual environment and install dependency:
```bash
python3 -m venv venv
source venv/bin/activate
pip install pynput
