class Vehicle:
    __COLOR_VARIANTS = ['red', 'green', 'black']

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец {self.owner}')

    def set_color(self, new_color: str):
        lower_new_color = new_color.lower()
        lower_variants = [i.lower() for i in self.__COLOR_VARIANTS]
        if lower_new_color in lower_variants:
            self.__color = new_color
            print(f'Цвет изменен на {new_color}')
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def get_model(self):
        return super().get_model()

    def get_horsepower(self):
        return super().get_horsepower()

    def get_color(self):
        return super().get_color()

    def print_info(self):
        return super().print_info()

    def set_color(self, new_color):
        super().set_color(new_color)

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()