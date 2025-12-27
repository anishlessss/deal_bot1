# Phase 1: Structure-only Amazon bot (no affiliate, no API)

from typing import List, Dict

print("🟠 AMAZON MODULE LOADED")

AMAZON_PRODUCTS = [
    {
        "title": "Echo Dot (5th Gen) Smart Speaker",
        "link": "https://www.amazon.in/dp/B09B8V1LZ3",
        "price": "Check on Amazon",
        "note": "Popular Amazon product"
    },
    {
        "title": "Redmi 12 5G Smartphone",
        "link": "https://www.amazon.in/dp/B0C9J5D6Y5",
        "price": "Check on Amazon",
        "note": "Trending mobile"
    },
    {
        "title": "Fire TV Stick 4K",
        "link": "https://www.amazon.in/dp/B08R6QR863",
        "price": "Check on Amazon",
        "note": "Streaming device"
    }
]

def get_amazon_products() -> List[Dict]:
    print("🟠 get_amazon_products() CALLED")
    return AMAZON_PRODUCTS
