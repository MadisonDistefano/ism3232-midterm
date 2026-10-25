# Author: Madison Distefano
from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    format_event_line,
    get_event_discount,
    largest_event,
    needs_second_chef,
    needs_signoff,
    total_booked,
)


def make_event(client, guest_price, guests, nonprofit=False):
    """Build one event record for a test."""
    return {
        "client": client,
        "guest_price": guest_price,
        "guests": guests,
        "nonprofit": nonprofit,
    }


# calculate_food_cost
def test_food_cost_is_price_times_guests():
    assert round(calculate_food_cost(18.00, 20), 2) == 360.00


# get_event_discount: limits at 25 guests and 100 guests
def test_discount_just_below_25_guests_is_zero():
    assert get_event_discount(24) == 0.0


def test_discount_at_25_guests_is_five_percent():
    assert get_event_discount(25) == 0.05


def test_discount_just_below_100_guests_for_nonprofit_is_five_percent():
    assert get_event_discount(99, True) == 0.05


def test_discount_at_100_guests_for_nonprofit_is_twelve_percent():
    assert get_event_discount(100, True) == 0.12


def test_discount_at_100_guests_not_nonprofit_is_five_percent():
    assert get_event_discount(100, False) == 0.05


def test_nonprofit_flag_changes_the_discount():
    assert get_event_discount(150, True) == 0.12
    assert get_event_discount(150, False) == 0.05


# calculate_event_total: fee limit at 500.00
def test_total_adds_service_fee_to_a_small_event():
    assert round(calculate_event_total(18.00, 20), 2) == 435.00


def test_total_adds_fee_when_cost_is_exactly_500():
    assert round(calculate_event_total(500.00, 1), 2) == 575.00


def test_total_has_no_fee_when_cost_is_just_above_500():
    assert round(calculate_event_total(500.01, 1), 2) == 500.01


def test_total_checks_the_fee_after_the_discount():
    assert round(calculate_event_total(21.00, 25), 2) == 573.75


def test_total_with_five_percent_discount_and_no_fee():
    assert round(calculate_event_total(20.00, 80), 2) == 1520.00


def test_total_for_nonprofit_gets_twelve_percent_off():
    assert round(calculate_event_total(25.00, 150, True), 2) == 3300.00


# needs_signoff: limit at 2500.00
def test_signoff_not_needed_at_exactly_2500():
    assert needs_signoff(2500.00) is False


def test_signoff_needed_just_above_2500():
    assert needs_signoff(2500.01) is True


# needs_second_chef: limits at 80 guests and 3000.00
def test_second_chef_not_needed_at_80_guests():
    assert needs_second_chef(80, 1000.00) is False


def test_second_chef_needed_at_81_guests():
    assert needs_second_chef(81, 1000.00) is True


def test_second_chef_not_needed_just_below_3000():
    assert needs_second_chef(10, 2999.99) is False


def test_second_chef_needed_at_exactly_3000():
    assert needs_second_chef(10, 3000.00) is True


# total_booked
def test_total_booked_adds_every_event():
    events = [
        make_event("Finch Law", 18.00, 20),
        make_event("Garden Club", 22.00, 40, True),
    ]
    assert round(total_booked(events), 2) == 1271.00


def test_total_booked_of_an_empty_list_is_zero():
    assert total_booked([]) == 0.0


# largest_event
def test_largest_event_returns_the_biggest_client():
    events = [
        make_event("Finch Law", 18.00, 20),
        make_event("Hilltop Gym", 30.00, 120),
        make_event("Juniper Spa", 16.00, 30),
    ]
    assert largest_event(events) == "Hilltop Gym"


def test_largest_event_tie_returns_the_first_in_the_list():
    events = [
        make_event("First Co", 20.00, 80),
        make_event("Second Co", 20.00, 80),
    ]
    assert largest_event(events) == "First Co"


def test_largest_event_of_an_empty_list_is_an_empty_string():
    assert largest_event([]) == ""


# format_event_line
def test_format_line_shows_yes_for_both():
    line = format_event_line("Hilltop Gym", 3420.00, True, True)
    assert line == "Hilltop Gym: $3420.00 | sign-off: yes | second chef: yes"


def test_format_line_shows_no_for_both():
    line = format_event_line("Finch Law", 435, False, False)
    assert line == "Finch Law: $435.00 | sign-off: no | second chef: no"


def test_format_line_shows_a_mix_of_yes_and_no():
    line = format_event_line("Lumen Labs", 1154.25, False, True)
    assert line == "Lumen Labs: $1154.25 | sign-off: no | second chef: yes"
