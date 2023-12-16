import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all: list = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.price = self.price * self.pay_rate
        Item.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]
        return None

    @classmethod
    def instantiate_from_csv(cls, file: str) -> list:
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv.
        """
        cur_dir = os.path.dirname(os.path.dirname(__file__))
        path_to_file = os.path.join(cur_dir + "/" + file)

        with open(path_to_file, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all = []
            reader_list = []
            for row in reader:
                name, price, quantity = row["name"], float(row["price"]), int(row["quantity"])
                reader_list.append(cls(name, price, quantity))
        return reader_list

    @staticmethod
    def string_to_number(dig_str: str) -> int:
        """
        Cтатический метод, возвращающий число из числа-строки/
        """
        return int(float(dig_str))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.total_price = self.price * self.quantity
        return self.total_price

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price
