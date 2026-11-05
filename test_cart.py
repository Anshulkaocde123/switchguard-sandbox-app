import pytest
from cart_service import calculate_cart_total

def test_empty_cart():
    assert calculate_cart_total([]) == 0.0

@pytest.mark.parametrize("items,expected_total", [
    ([], 0.0),
    ([{"price": 10.0, "quantity": 1}], 10.0),
    ([{"price": 15.5}], 15.5),
    ([{"price": 25.0, "quantity": 2}, {"price": 10.0, "quantity": 1}], 60.0),
    ([{"price": 0.0, "quantity": 5}], 0.0),
    ([{"price": 100.0, "quantity": 1}, {"price": 200.0, "quantity": 2}], 500.0),
])
def test_standard_checkout_without_discount(items, expected_total):
    assert calculate_cart_total(items) == expected_total

@pytest.mark.parametrize("items,discount_code,expected_total", [
    ([{"price": 50.0, "quantity": 1}], "UNKNOWN", 50.0),
    ([{"price": 75.0, "quantity": 1}], "", 75.0),
    ([{"price": 30.0, "quantity": 2}], None, 60.0),
])
def test_unknown_or_empty_discount_code(items, discount_code, expected_total):
    assert calculate_cart_total(items, discount_code=discount_code) == expected_total

@pytest.mark.parametrize("items,expected_total", [
    ([{"price": 100.0, "quantity": 1}], 0.0),
    ([{"price": 50.0, "quantity": 2}], 0.0),
    ([{"price": 100.01, "quantity": 1}], 0.01),
    ([{"price": 75.0, "quantity": 2}], 50.0),
    ([{"price": 200.0, "quantity": 1}], 100.0),
    ([{"price": 250.0, "quantity": 2}], 400.0),
])
def test_flat100_boundary_applied_at_and_above_threshold(items, expected_total):
    assert calculate_cart_total(items, discount_code="FLAT100") == pytest.approx(expected_total)
