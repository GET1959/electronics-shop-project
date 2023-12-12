from src.item import Item
import pytest

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

    def apply_discount():
        assert item1.apply_discount() == 8000.0
        assert item2.apply_discount() == 20000