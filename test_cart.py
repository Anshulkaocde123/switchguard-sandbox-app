import pytest
from cart_service import calculate_cart_total

def test_empty_cart():
    assert calculate_cart_total([]) == 0.0

def test_standard_checkout_without_discount():
    items = [{"price": 25.0, "quantity": 2}, {"price": 10.0, "quantity": 1}]
    assert calculate_cart_total(items) == 60.0

def test_flat100_standard_applied_above_threshold():
    items = [{"price": 75.0, "quantity": 2}]
    assert calculate_cart_total(items, discount_code="FLAT100") == 50.0
