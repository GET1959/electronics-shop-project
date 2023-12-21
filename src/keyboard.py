from src.item import Item


class MixinLanguage:
    def __init__(self) -> None:
        self.__language = "EN"

    @property
    def language(self) -> str:
        return self.__language

    def change_lang(self) -> None:
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(Item, MixinLanguage):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        MixinLanguage.__init__(self)
