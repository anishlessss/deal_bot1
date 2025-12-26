from feeds import fetch_feed_items
import re
import urllib.parse

def make_flipkart_search_link(title):
    query = urllib.parse.quote_plus(title)
    return f"https://www.flipkart.com/search?q={query}"

def extract_price(text):
    match = re.search(r"₹\s?[\d,]+", text)
    return match.group(0) if match else "Check on Flipkart"

def extract_discount(text):
    match = re.search(r"\d{1,2}%\s?off", text, re.I)
    return match.group(0).upper() if match else "Deal Live"

def get_deals():
    deals = []
    items = fetch_feed_items()

    for item in items:
        text = f"{item['title']} {item['summary']}".lower()

        # Keep only Flipkart-related deals
        if "flipkart" not in text:
            continue

        title = item["title"].strip()
        price = extract_price(item["title"] + item["summary"])
        discount = extract_discount(item["title"] + item["summary"])

        deals.append({
            "title": title,
            "price": price,
            "discount": discount,
            # IMPORTANT: use Flipkart search link, not feed link
            "link": make_flipkart_search_link(title)
        })

    return deals
