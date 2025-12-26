import schedule
import time
from main import run_bot

print("🤖 Deal bot scheduler started...")

schedule.every(1).hours.do(run_bot)

while True:
    schedule.run_pending()
    time.sleep(10)
