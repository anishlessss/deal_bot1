from deals import get_deals
from telegram import send
from dedupe import load_sent, mark_sent
from amazon import get_amazon_products

MAX_POSTS_PER_RUN = 5

def run_bot():
    print("🔍 Checking Flipkart deals...")
    sent_links = load_sent()
    new_count = 0

    # -------- FLIPKART --------
    flipkart_deals = get_deals()

    for deal in flipkart_deals:
        link = deal.get("link", "").strip()
        title = deal.get("title", "").strip()
        price = deal.get("price", "Check on Flipkart")
        discount = deal.get("discount", "Deal Live")

        if not link or link in sent_links:
            continue

        message = (
            "🔥 FLIPKART DEAL 🔥\n\n"
            f"🛍️ {title}\n"
            f"💰 Price: {price}\n"
            f"📉 Discount: {discount}\n\n"
            f"👉 Buy now:\n{link}"
        )

        send(message)
        mark_sent(link)
        sent_links.add(link)

        new_count += 1
        print("📨 Sent Flipkart:", title)

        if new_count >= MAX_POSTS_PER_RUN:
            return

    # -------- AMAZON (STRUCTURE MODE) --------
    print("🔍 Checking Amazon products...")
    amazon_products = get_amazon_products()

    for product in amazon_products:
        link = product["link"]

        if link in sent_links:
            continue

        message = (
            "🟠 AMAZON PRODUCT 🟠\n\n"
            f"🛍️ {product['title']}\n"
            f"💰 {product['price']}\n"
            f"ℹ️ {product['note']}\n\n"
            f"👉 View on Amazon:\n{link}"
        )

        send(message)
        mark_sent(link)
        sent_links.add(link)

        print("📨 Sent Amazon:", product["title"])
        return

    print("ℹ️ No new deals found.")

if __name__ == "__main__":
    run_bot()
