import time

from deals import get_deals
from telegram import send
from dedupe import load_sent, mark_sent

# how many deals to post per run
MAX_POSTS_PER_RUN = 5

# run every 1 hour
INTERVAL_SECONDS = 60 * 60


def run_bot():
    print("🔍 Checking Flipkart deals...")

    sent_links = load_sent()
    deals = get_deals()

    if not deals:
        print("ℹ️ No deals fetched.")
        return

    new_count = 0

    for deal in deals:
        link = deal.get("link", "").strip()
        title = deal.get("title", "").strip()
        price = deal.get("price", "Check on Flipkart")
        discount = deal.get("discount", "Deal Live")

        if not link or link in sent_links:
            continue

        message = (
            "🔥 FLIPKART DEAL 🔥\n\n"
            f"🛍️ {title}\n"
            f"💰 Price: {price}* (may vary)\n"
            f"📉 Discount: {discount}\n\n"
            f"👉 Buy now:\n{link}"
        )

        send(message)
        mark_sent(link)
        sent_links.add(link)

        new_count += 1
        print("📨 Sent:", title)

        if new_count >= MAX_POSTS_PER_RUN:
            break

    if new_count == 0:
        print("ℹ️ No new deals found.")


if __name__ == "__main__":
    while True:
        run_bot()
        print("⏰ Sleeping for 1 hour...\n")
        time.sleep(INTERVAL_SECONDS)

