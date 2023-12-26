import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
Item.pay_rate = 0.9


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    assert item1.apply_discount() == 9000.0
    assert item2.apply_discount() == 18000.0


def test_instantiate_from_csv():
    assert [item.name for item in Item.instantiate_from_csv("src/items.csv")] == [
        "Смартфон",
        "Ноутбук",
        "Кабель",
        "Мышка",
        "Клавиатура",
    ]


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5


@pytest.mark.parametrize(
    "arg, expected", [(Item("Смартфон", 10000, 20), "Item('Смартфон', 10000, 20)")]
)
def test_repr(arg, expected):
    assert repr(arg) == expected


def test_str():
    assert str(item1) == "Смартфон"


item3 = Item("Смартфон", 10000, 20)
phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_add():
    assert item3 + phone1 == 25
    assert phone1 + phone1 == 10


def test_instantiate_from_csv_not_found():
    try:
        Item.instantiate_from_csv("item.csv")
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")


def test_instantiate_from_csv_er():
    with pytest.raises(InstantiateCSVError, match="Файл item.csv поврежден"):
        Item.instantiate_from_csv("/src/item.csv")
