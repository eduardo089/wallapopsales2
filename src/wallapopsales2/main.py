from wallapy import check_wallapop

def main():
    results = check_wallapop(
        product_name="iPhone 15",
        keywords=["iphone", "15", "pro", "128gb", "unlocked"],
        min_price=500,
        max_price=800,
        excluded_keywords=["broken", "repair", "cracked screen"],
        max_total_items=50,
        order_by="price_low_to_high",
    )

    if not results:
        print("No results found.")
        return

    for ad in results:
        print(ad["title"], ad["price"], ad.get("location"), ad["link"])


if __name__ == "__main__":
    main()