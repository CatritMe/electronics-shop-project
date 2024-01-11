"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone


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


def test_repr(soap):
    assert repr(soap) == "Item('Soap', 50, 1000)"


def test_str(soap):
    assert str(soap) == 'Soap'


def test_add():
    item1 = Item('Ноутбук', 70000, 10)
    phone1 = Phone('iPhone', 50000, 20, 2)
    assert item1 + phone1 == 30
    assert phone1 + phone1 == 40
    with pytest.raises(TypeError):
        123 + item1


def test_instantiate_from_csv_error():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('path')


def test_instantiate_from_csv_failed_file():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('tests/failed_items.csv')