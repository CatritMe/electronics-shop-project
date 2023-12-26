from src.item import Item

class Phone(Item):
    """
    Класс для представления телефонов в магазине.
    """

    def __init__(self, name, price, quantity, number_of_sim):
        """
        Создание экземпляра класса item.
        :param name, price, quantity - наследуемые
        :param number_of_sim - количество поддерживаемых сим-карт
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim
    @number_of_sim.setter
    def number_of_sim(self, value):
        if value > 0:
            self.__number_of_sim = value
        raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")

