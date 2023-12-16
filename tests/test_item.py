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


def test_name(soap):
    assert soap.name == 'Soap'
    soap.name = 'Soapthebest'
    assert soap.name == 'Soapthebes'

def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

def test_string_to_number():
    assert Item.string_to_number('123.5') == 123