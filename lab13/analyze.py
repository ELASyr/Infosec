#!/usr/bin/env python3


from collections import Counter
import os, re

LOG_DIR = "collected"

def read_logs():
    texts = []
    if not os.path.exists(LOG_DIR):
        return texts
    for f in sorted(os.listdir(LOG_DIR)):
        path = os.path.join(LOG_DIR, f)
        if os.path.isfile(path):
            with open(path, encoding="utf-8") as fh:
                texts.append(fh.read())
    return "\n".join(texts)

def tokenize(text):
    return re.findall(r"[A-Za-z0-9]+", text)

def main():
    data = read_logs()
    if not data.strip():
        print("No log data found in collected/. Run main.py first.")
        return
    tokens = tokenize(data)
    c = Counter(tokens)
    print("Top 20 tokens:")
    for token, count in c.most_common(20):
        print(f"{token}  {count}")

if __name__ == "__main__":
    main()
