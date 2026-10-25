# business_rules.py
# Author: Madison Distefano

BASIC_DISCOUNT_GUESTS = 25
NONPROFIT_GUESTS = 100
BASIC_RATE = 0.05
NONPROFIT_RATE = 0.12
SERVICE_FEE = 75.00
SERVICE_FEE_LIMIT = 500.00
SIGNOFF_LIMIT = 2500.00
SECOND_CHEF_GUESTS = 80
SECOND_CHEF_TOTAL = 3000.00


def calculate_food_cost(guest_price: float, guests: int) -> float:
    """Return the food cost before any discount."""
    return round(guest_price * guests, 2)


def get_event_discount(guests: int, nonprofit: bool = False) -> float:
    """Return the discount rate as a decimal."""
    if guests >= NONPROFIT_GUESTS and nonprofit:
        return NONPROFIT_RATE
    elif guests >= BASIC_DISCOUNT_GUESTS:
        return BASIC_RATE
    else:
        return 0.0


def calculate_event_total(
    guest_price: float, guests: int, nonprofit: bool = False
) -> float:
    """Return the discounted cost plus the service fee when it applies."""
    food_cost = calculate_food_cost(guest_price, guests)
    rate = get_event_discount(guests, nonprofit)
    total = round(food_cost * (1 - rate), 2)
    if total <= SERVICE_FEE_LIMIT:
        total = total + SERVICE_FEE
    return round(total, 2)


def needs_signoff(total: float) -> bool:
    """Return True when the event total needs a manager's sign-off."""
    return total > SIGNOFF_LIMIT


def needs_second_chef(guests: int, total: float) -> bool:
    """Return True when the event needs a second chef."""
    return guests > SECOND_CHEF_GUESTS or total >= SECOND_CHEF_TOTAL


def total_booked(events: list) -> float:
    """Return the sum of the event totals for every event in the list."""
    booked = 0.0
    for event in events:
        booked += calculate_event_total(
            event["guest_price"], event["guests"], event["nonprofit"]
        )
    return round(booked, 2)


def largest_event(events: list) -> str:
    """Return the client with the largest event total, or an empty string."""
    largest_client = ""
    largest_total = 0.0
    for event in events:
        total = calculate_event_total(
            event["guest_price"], event["guests"], event["nonprofit"]
        )
        if total > largest_total:
            largest_client = event["client"]
            largest_total = total
    return largest_client


def format_event_line(
    client: str, total: float, signoff: bool, second_chef: bool
) -> str:
    """Return one line of the event report."""
    if signoff:
        signoff_text = "yes"
    else:
        signoff_text = "no"
    if second_chef:
        chef_text = "yes"
    else:
        chef_text = "no"
    line = f"{client}: ${total:.2f}"
    return f"{line} | sign-off: {signoff_text} | second chef: {chef_text}"
