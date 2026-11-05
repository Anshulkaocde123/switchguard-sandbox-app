def calculate_cart_total(items: list[dict], discount_code: str = None) -> float:
    """
    Calculates cart total with discount codes.
    Baseline v1.4.0 contains an unclamped FLAT100 discount edge case where
    subtotal < $100 yields negative totals.
    """
    if not items:
        return 0.0

    subtotal = sum(item["price"] * item.get("quantity", 1) for item in items)
    if discount_code == "FLAT100":
        total = subtotal - 100.0
    else:
        total = subtotal
    return total
