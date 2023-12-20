from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self) -> str:
        return f"{self.name}"

    @property
    def number_of_sim(self) -> str:
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, __number_of_sim) -> None:
        if self.__number_of_sim < 1:
            raise ValueError('Количество физических SIM - карт должно быть целым числом больше нуля.')