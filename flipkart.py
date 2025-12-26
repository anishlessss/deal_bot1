from browser import open_page

def get_flipkart_deals():
    url = "https://www.flipkart.com/search?q=mobile"

    p, browser, page = open_page(url)
    deals = []

    try:
        # close login popup if present
        try:
            page.click("button._2KpZ6l._2doB4z", timeout=3000)
            print("Login popup closed")
        except:
            pass

        # scroll to force JS to attach links
        page.mouse.wheel(0, 3000)
        page.wait_for_timeout(5000)

        page.wait_for_selector("div[data-id]", timeout=30000)
        products = page.query_selector_all("div[data-id]")

        print("Found products:", len(products))

        for product in products[:5]:
            title_el = (
                product.query_selector("div._4rR01T")
                or product.query_selector("a.s1Q9rs")
            )
            price_el = product.query_selector("div._30jeq3")

            # IMPORTANT: wait for link INSIDE product
            link_el = product.query_selector("a[href*='/p/']")

            if not price_el or not link_el:
                continue

            title = title_el.inner_text().strip() if title_el else "Flipkart Product"
            price = price_el.inner_text().strip()
            href = link_el.get_attribute("href")

            if not href:
                continue

            link = "https://www.flipkart.com" + href
            deals.append((title, price, link))
            print("→ Prepared:", title)

    finally:
        browser.close()
        p.stop()

    return deals
