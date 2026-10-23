
BULK_PLATES = 5
PARTY_PLATES = 10
BULK_RATE = 0.15
PARTY_RATE = 0.20
SMALL_ORDER_LIMIT = 40.00
SMALL_ORDER_FEE = 5.00
TAX_RATE = 0.075
BIG_ORDER_LIMIT = 100.00


def calculate_subtotal(price: float, plates: int) -> float:
    """Return the plate price times the number of plates."""
    return round(price * plates, 2)


def get_discount_rate(plates: int, birthday: bool = False) -> float:
    """Return the discount rate as a decimal."""
    if plates >= PARTY_PLATES and birthday:
        return PARTY_RATE
    elif plates >= BULK_PLATES:
        return BULK_RATE
    else:
        return 0.0


def calculate_small_order_fee(discounted: float) -> float:
    """Return the small order fee, or 0 if the cost is not below the limit."""
    if discounted < SMALL_ORDER_LIMIT:
        return SMALL_ORDER_FEE
    return 0.0


def calculate_order_total(price: float, plates: int, birthday: bool = False) -> float:
    """Return the total after discount, small order fee, and tax."""
    subtotal = calculate_subtotal(price, plates)
    rate = get_discount_rate(plates, birthday)
    discounted = round(subtotal * (1 - rate), 2)
    taxable = discounted + calculate_small_order_fee(discounted)
    tax = round(taxable * TAX_RATE, 2)
    return round(taxable + tax, 2)


def is_big_order(total: float) -> bool:
    """Return True if the total is at or above the big order limit."""
    return total >= BIG_ORDER_LIMIT


def total_revenue(orders: list[dict]) -> float:
    """Return the sum of every order total in the list."""
    revenue = 0.0
    for order in orders:
        revenue += calculate_order_total(
            order["price"], order["plates"], order["birthday"]
        )
    return round(revenue, 2)


def find_largest_order(orders: list[dict]) -> dict | None:
    """Return the order with the largest total, or None for an empty list."""
    largest = None
    largest_total = 0.0
    for order in orders:
        total = calculate_order_total(
            order["price"], order["plates"], order["birthday"]
        )
        if largest is None or total > largest_total:
            largest = order
            largest_total = total
    return largest


def format_order_line(order: dict, total: float) -> str:
    """Return one report line for an order."""
    return f"{order['order_id']} | {order['guest']}: ${total:.2f}"