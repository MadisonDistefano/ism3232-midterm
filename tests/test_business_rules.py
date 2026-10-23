# Author: Madison Distefano
from business_rules import (
    calculate_order_total,
    calculate_small_order_fee,
    calculate_subtotal,
    find_largest_order,
    format_order_line,
    get_discount_rate,
    is_big_order,
    total_revenue,
)


def make_order(order_id, price, plates, birthday=False):
    """Build one order record for a test."""
    return {
        "order_id": order_id,
        "guest": "Guest " + order_id,
        "price": price,
        "plates": plates,
        "birthday": birthday,
    }


# calculate_subtotal


def test_subtotal_multiplies_price_by_plates():
    assert calculate_subtotal(24.99, 3) == 74.97


# get_discount_rate: limit at 5 plates, limit at 10 plates


def test_rate_just_below_bulk_limit_is_zero():
    assert get_discount_rate(4) == 0.0


def test_rate_at_bulk_limit_is_bulk_rate():
    assert get_discount_rate(5) == 0.15


def test_rate_just_below_party_limit_with_birthday_is_bulk_rate():
    assert get_discount_rate(9, True) == 0.15


def test_rate_at_party_limit_with_birthday_is_party_rate():
    assert get_discount_rate(10, True) == 0.20


def test_rate_at_party_limit_without_birthday_is_bulk_rate():
    assert get_discount_rate(10, False) == 0.15


# calculate_small_order_fee: limit at 40.00


def test_fee_just_below_limit_is_charged():
    assert calculate_small_order_fee(39.99) == 5.00


def test_fee_at_limit_is_not_charged():
    assert calculate_small_order_fee(40.00) == 0.0


# calculate_order_total


def test_total_small_order_includes_fee_and_tax():
    assert calculate_order_total(9.99, 3) == 37.59


def test_total_just_below_fee_limit_adds_fee():
    assert calculate_order_total(9.99, 4) == 48.33


def test_total_at_fee_limit_has_no_fee():
    assert calculate_order_total(10.00, 4) == 43.00


def test_total_with_no_discount_adds_tax_only():
    assert calculate_order_total(30.00, 4) == 129.00


def test_total_bulk_discount_applies_before_tax():
    assert calculate_order_total(18.00, 5) == 82.24


def test_total_party_with_birthday_gets_party_rate():
    assert calculate_order_total(20.00, 10, True) == 172.00


def test_total_party_without_birthday_gets_bulk_rate():
    assert calculate_order_total(20.00, 10, False) == 182.75


# is_big_order: limit at 100.00


def test_big_order_just_below_limit_is_false():
    assert is_big_order(99.99) is False


def test_big_order_at_limit_is_true():
    assert is_big_order(100.00) is True


# total_revenue


def test_revenue_adds_every_order():
    orders = [make_order("A", 9.99, 3), make_order("B", 20.00, 10, True)]
    assert total_revenue(orders) == 209.59


def test_revenue_of_empty_list_is_zero():
    assert total_revenue([]) == 0.0


# find_largest_order


def test_largest_order_is_found_in_the_middle():
    small = make_order("A", 9.99, 3)
    big = make_order("B", 20.00, 10, True)
    medium = make_order("C", 30.00, 4)
    assert find_largest_order([small, big, medium]) == big


def test_largest_order_is_found_at_the_end():
    small = make_order("A", 9.99, 3)
    big = make_order("B", 20.00, 10, True)
    assert find_largest_order([small, big]) == big


def test_largest_order_tie_returns_the_first():
    first = make_order("A", 30.00, 4)
    second = make_order("B", 30.00, 4)
    assert find_largest_order([first, second]) is first


def test_largest_order_of_empty_list_is_none():
    assert find_largest_order([]) is None


# format_order_line


def test_format_line_shows_id_guest_and_total():
    order = make_order("LH-1001", 24.99, 1)
    order["guest"] = "Table A"
    assert format_order_line(order, 32.24) == "LH-1001 | Table A: $32.24"


def test_format_line_always_shows_two_decimals():
    order = make_order("LH-1002", 5.00, 1)
    order["guest"] = "Table B"
    assert format_order_line(order, 5) == "LH-1002 | Table B: $5.00"