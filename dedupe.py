import os

FILE_PATH = "sent_links.txt"

def load_sent():
    if not os.path.exists(FILE_PATH):
        return set()
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())

def mark_sent(link):
    with open(FILE_PATH, "a", encoding="utf-8") as f:
        f.write(link + "\n")
