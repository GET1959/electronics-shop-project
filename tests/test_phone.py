import pytest

from src.phone import Phone


@pytest.mark.parametrize(
    "arg, expected", [(Phone("iPhone 14", 120_000, 5, 2), "Phone('iPhone 14', 120000, 5, 2)")]
)
def test_repr(arg, expected):
    assert repr(arg) == expected


phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_str():
    assert str(phone1) == "iPhone 14"
