from deals import get_deals
from telegram import send
from dedupe import load_sent, mark_sent
from amazon import get_amazon_products

MAX_FLIPKART_POSTS = 3
MAX_AMAZON_POSTS = 1

def run_bot():
    sent_links = load_sent()

    # ---------- FLIPKART ----------
    print("🔍 Checking Flipkart deals...")
    fk_sent = 0
    flipkart_deals = get_deals()

    for deal in flipkart_deals:
        if fk_sent >= MAX_FLIPKART_POSTS:
            break

        link = deal.get("link")
        if not link or link in sent_links:
            continue

        message = (
            "🔥 FLIPKART DEAL 🔥\n\n"
            f"🛍️ {deal.get('title')}\n"
            f"💰 Price: {deal.get('price')}\n"
            f"📉 Discount: {deal.get('discount')}\n\n"
            f"👉 Buy now:\n{link}"
        )

        send(message)
        mark_sent(link)
        sent_links.add(link)
        fk_sent += 1

        print("📨 Sent Flipkart:", deal.get("title"))

    # ---------- AMAZON ----------
    print("🔍 Checking Amazon products...")
    az_sent = 0
    amazon_products = get_amazon_products()

    for product in amazon_products:
        if az_sent >= MAX_AMAZON_POSTS:
            break

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
        az_sent += 1

        print("📨 Sent Amazon:", product["title"])

    print("✅ Run complete.")

if __name__ == "__main__":
    run_bot()
