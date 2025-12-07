# Lab 12 — Brute-force attacks (Infosec)

**PS:** Only run these exercises on systems you own or have explicit permission to test.

## Goal
Demonstrate a local dictionary brute‑force attack against a simple FastAPI login endpoint and create / test targeted wordlists derived from victim info.

## Files in this folder
- `main.py` — FastAPI vulnerable server (POST `/login`).
- `usernames.txt` — Username wordlist used for testing.
- `passwords.txt` — Common password list used for testing.
- `generate_wordlist.py` — Small Python script to produce targeted password candidates (name/surname/dob combos).
- `john-doe-passwords.txt` — Example generated list (if created).
- `lab12-report.md` — Report with results and notes.
- `hydra-output.txt` — (optional) Hydra output saved for evidence.
