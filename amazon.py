# Phase 1: Structure-only Amazon bot (no affiliate, no API)

from typing import List, Dict

# Temporary static products for learning
# Later this will be replaced by Amazon API results
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
    }
]

def get_amazon_products() -> List[Dict]:
    """
    Returns a list of Amazon products.
    Later this function will call Amazon Product Advertising API.
    """
    return AMAZON_PRODUCTS