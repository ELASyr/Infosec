#!/usr/bin/env python3


import os, shutil
SRC = "collected"
DST = "sent"

os.makedirs(SRC, exist_ok=True)
os.makedirs(DST, exist_ok=True)

files = [f for f in os.listdir(SRC) if f.startswith("log")]
if not files:
    print("No files to simulate upload.")
else:
    for f in files:
        srcp = os.path.join(SRC, f)
        dstp = os.path.join(DST, f)
        shutil.move(srcp, dstp)
        print(f"Moved {srcp} -> {dstp}")
print("Simulated upload finished. Files are in ./sent/")
