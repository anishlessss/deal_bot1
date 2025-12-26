import feedparser

FEEDS = [
    # Major Indian deal communities
    "https://feeds.feedburner.com/DesiDime",
    "https://feeds.feedburner.com/dealsshutter",

    # Extra high-activity feeds
    "https://feeds.feedburner.com/DealsMagnet",
    "https://feeds.feedburner.com/DealBeeIndia",
    "https://feeds.feedburner.com/OfferDiary",

    # Mixed ecommerce deals (Flipkart + Amazon)
    "https://www.grabon.in/rss/",
]

def fetch_feed_items():
    items = []

    for url in FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries:
            items.append({
                "title": entry.get("title", ""),
                "summary": entry.get("summary", ""),
                "link": entry.get("link", "")
            })

    return items
