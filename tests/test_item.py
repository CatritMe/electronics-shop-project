"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def soap():
    return Item('Soap', 50, 1000)


def test_calculate_total_price(soap):
    assert soap.calculate_total_price() == 50000


def test_apply_discount(soap):
    assert soap.apply_discount() == 50
