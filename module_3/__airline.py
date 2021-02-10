'''
* Определить пользовательский класс.
* определить в классе следующие конструкторы: с параметрами и без параметров
* компоненты-функции для просмотра и установки полей данных: setТип(), getТип()
- (помним про инкапсуляцию проверку корректности задания параметров);
написать демонстрационную программу, в которой создаются и разрушаются объекты (от 3 до 5 шт.)
и указатели на объекты пользовательского класса и каждый вызов конструктора
сопровождается выдачей соответствующего сообщения.
использовать метод __setattr__()
не забывайте выполнять задание, выделенное курсивом в варианте.

Создать класс Airline: Пункт назначения, Номер рейса, Тип самолета, Время вылета, Дни недели.
Функции - члены реализуют запись и считывание полей (проверка корректности).
Создать список объектов.
Вывести:
--список рейсов для заданного пункта назначения;
--список рейсов для заданного дня недели;
'''


class Airline:
    license = 'qijijofndncc'

    def __init__(self,
                 destination='Минск',
                 flight_number='2390',
                 aircraft_type='Boeing 737-300',
                 time='00:00',
                 week_days=['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']):

        self.__destination = destination
        self.__flight_number = flight_number
        self.__aircraft_type = aircraft_type
        self.__departure_time = time
        self.__departure_days = week_days
        print('Вызван конструктор __init__')

    def __del__(self):  # Деструктор класса
        print('Вызван метод __del__()')

    def __setattr__(self, attr, value):
        if attr != 'license':
            self.__dict__[attr] = value
        else:
            raise AttributeError

    def get_destination(self):
        return self.__destination

    def set_destination(self, destination):
        self.__destination = destination

    def get_flight_number(self):
        return self.__flight_number

    def set_flight_number(self, flight_number):
        self.__flight_number = flight_number

    def get_aircraft_type(self):
        return self.__aircraft_type

    def set_aircraft_type(self, aircraft_type):
        self.__aircraft_type = aircraft_type

    def get_departure_time(self):
        return self.__departure_time

    def set_departure_time(self, departure_time):
        self.__departure_time = departure_time

    def get_departure_days(self):
        return self.__departure_days

    def set_departure_days(self, departure_days):
        self.__departure_days = departure_days


airline_list = [
    Airline(),
    Airline('Тель-Авив', '2345', 'Boeing 737-800', '21:20', ['пн', 'сб']),
    Airline('Москва', '7845', 'Boeing 737-900', '14:35', ['вт', 'чт', 'сб']),
    Airline('Вильнюс', '9945', 'Embraer 175', '12:15', ['вт', 'чт']),
    Airline('Хургада', '3245', 'Boeing 737-300', '02:05', ['пн', 'сб']),
    Airline('Киев', '8945', 'Embraer 195', '08:15', ['вс']),
    Airline('Варшава', '1345', 'Boeing 737-800', '21:20', ['пн', 'сб']),
    Airline('Хургада', '3845', 'Boeing 737-900', '14:35', ['вт', 'чт', 'сб']),
    Airline('Рим', '4945', 'Embraer 175', '12:15', ['вт', 'чт']),
    Airline('Лондон', '7245', 'Boeing 737-300', '02:05', ['пн', 'сб']),
    Airline('Берлин', '3945', 'Embraer 195', '07:15', ['вс'])
]


def print_list(obj_list, param):
    if len(obj_list) > 0:
        print(f'Результат по критерию "{param}":')
        for obj in obj_list:
            print(obj.get_flight_number(), ' - ', obj.get_destination(), ' - ', " ".join(obj.get_departure_days()))
        return


def show_result(arg, lambda_exp):
    filter_result = list(filter(lambda_exp, airline_list))
    print_list(filter_result, arg) if len(filter_result) > 0 else print('Данных по запросу не найдено')


destination_city_request = input('Введите пункт назначения: \n')
show_result(destination_city_request, lambda x: x.get_destination() == destination_city_request)

day_of_week_request = input('Введите день недели в формате "пн", "вт", "ср", "чт", "пт", "сб", "вс": \n')
show_result(day_of_week_request, lambda x: day_of_week_request in x.get_departure_days())
