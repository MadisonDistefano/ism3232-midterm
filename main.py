# main.py
from business_rules import (
    calculate_order_total,
    find_largest_order,
    format_order_line,
    get_discount_rate,
    is_big_order,
    total_revenue,
)

orders = [
    {
        "order_id": "LH-1001",
        "guest": "Table A",
        "price": 24.99,
        "plates": 1,
        "birthday": False,
    },
    {
        "order_id": "LH-1002",
        "guest": "Takeout B",
        "price": 18.99,
        "plates": 6,
        "birthday": False,
    },
    {
        "order_id": "LH-1003",
        "guest": "Table C",
        "price": 32.99,
        "plates": 2,
        "birthday": False,
    },
    {
        "order_id": "LH-1004",
        "guest": "Party D",
        "price": 21.99,
        "plates": 12,
        "birthday": True,
    },
    {
        "order_id": "LH-1005",
        "guest": "Table E",
        "price": 9.99,
        "plates": 3,
        "birthday": False,
    },
]

print("LONGHORN-INSPIRED ORDER REPORT")
print("=" * 42)

big_orders = 0
discounted_orders = 0
for order in orders:
    total = calculate_order_total(order["price"], order["plates"], order["birthday"])
    print(format_order_line(order, total))
    if is_big_order(total):
        big_orders += 1
    if get_discount_rate(order["plates"], order["birthday"]) > 0:
        discounted_orders += 1

revenue = total_revenue(orders)
largest = find_largest_order(orders)
largest_total = calculate_order_total(
    largest["price"], largest["plates"], largest["birthday"]
)

print("-" * 42)
print(f"Orders:         {len(orders)}")
print(f"Total revenue:  ${revenue:.2f}")
print(f"Average order:  ${revenue / len(orders):.2f}")
print(f"Largest order:  {format_order_line(largest, largest_total)}")
print(f"Big orders:     {big_orders}")
print(f"Discounted:     {discounted_orders}")