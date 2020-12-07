# Создать класс Car: id, Марка, Модель, Год выпуска, Цвет, Цена, Регистрационный номер. Функции-
# члены реализуют запись и считывание полей (проверка корректности), вывода возраста машины.
# Создать список объектов. Вывести:
# a) список автомобилей заданной марки;
# b) список автомобилей заданной модели, которые эксплуатируются больше n лет;

class Car:

    def __init__(self, mark, model, year, colour, price, reg_number):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__colour = colour
        self.__price = price
        self.__reg_number = reg_number

    def get_mark(self):
        return self.__mark

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_colour(self):
        return self.__colour

    def get_price(self):
        return self.__price

    def get_reg_number(self):
        return self.__reg_number

    def show_car(self):
        print('\t Mark:', self.get_mark(), '\t Model:', self.get_model(), '\t Year: ', self.get_year(),
              '\n \t Colour: ', self.get_colour(), '\t Price', self.get_price(), '\t Reg number: ',
              self.get_reg_number())


class Cars:
    __list_of_cars = []

    def add_car(self, new_car):
        self.__list_of_cars.append(new_car)

    def find_needed_mark(self, mark):
        res = list(filter(lambda x: x.get_mark() == mark, self.__list_of_cars))
        for i in res:
            i.show_car()

    def find_old_model_car(self, model, year):
        new_res = list(filter(lambda x: x.get_model() == model and x.get_year() < (2020 - year), self.__list_of_cars))
        for i in new_res:
            i.show_car()


Car = [
    Car('Lexus', 'RX350', 2018, 'Grey', 13000, '8714'),
    Car('Opel', 'KJ39', 2015, 'White', 12550, '1343'),
    Car('Ford', 'Focus', 2013, 'Blue', 12000, '1920'),
    Car('Lexus', 'DD192', 2017, 'Red', 14000, '8731'),
    Car('Audi', 'Focus', 2012, 'Green', 18000, '0909')]

all_of_cars = Cars()

for i in range(len(Car)):
    all_of_cars.add_car((Car[i]))

all_of_cars.find_needed_mark('Lexus')
print('')
all_of_cars.find_old_model_car('Focus', 3)
