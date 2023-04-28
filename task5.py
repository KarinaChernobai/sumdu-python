# Написати програму, яка створює словник для збереження даних із заданої предметної області та виконує обробку даних.
# Задано назви n=10 країн із загальною інформацією про них (площа, населення) і про частини світу, де вони розташовані.
# Скласти програму, яка визначає, чи є серед заданих країн ті, що знаходяться в Африці або в Азії.
# У разі позитивної відповіді надрукувати їх назви.

class Country:
    def __init__(self, location, area, population):
        self.location = location
        self.area = area
        self.population = population


countries = {
    "Ukraine": Country("Europe", 603628, 36744636),
    "Romania": Country("Europe", 238397, 18877397),
    "Israel": Country("Middle East", 22145, 9036028),
    "Switzerland": Country("Europe", 41290, 8832417),
    "Germany": Country("Europe", 357580, 84536211),
    "Singapore": Country("Asia", 7331, 5979599),
    "Luxembourg": Country("Europe", 2590, 654606),
    "Japan": Country("Asia", 377973, 125388972),
    "Botswana": Country("Africa", 581730, 2485007),
    "Rwanda": Country("Africa", 26338, 13855278),
}


def init_countries():
    print("Якщо ви хочете вивести усі значення словника, тоді натисніть -> 1 <-")
    print("Якщо ви хочете додати новий запис до словника, тоді натисніть -> 2 <-")
    print("Якщо ви хочете видалити запис зі словника, тоді натисніть -> 3 <-")
    print("Якщо ви хочете переглянути вміст словника за відсортованими ключами, тоді натисніть -> 4 <-")
    print("Якщо ви хочете дізнатися чи є серед заданих країн ті, що знаходяться в Африці, тоді натисніть -> 5 <-")
    print("Якщо ви хочете дізнатися чи є серед заданих країн ті, що знаходяться в Азії, тоді натисніть -> 6 <-")
    print("Якщо ви хочете вийти з програми, тоді натисніть -> 0 <-")
    while True:
        action = int(input("Введіть пункт меню: "))
        if action < 0 or action > 6:
            print("Ви ввели невірну опцію.")
            continue

        match action:
            case 0:
                break
            case 1:
                print_countries()
            case 2:
                add_country()
            case 3:
                _del_country()
            case 4:
                sort_countries()
            case 5:
                get_country_by_location("Africa")
            case 6:
                get_country_by_location("Asia")
            case _:
                raise Exception("You've entered the wrong code")
        print()

def print_countries():
    for key, value in countries.items():
        print_country(key, value)


def print_country(key, value):
    print('\033[1m', key, '\033[0m')
    print("частина світу:", value.location)
    print("площа:", value.area)
    print("населення:", value.population)
    print()


def add_country():
    key = input("Введіть країну, яку хочете додати до словника: ")
    location = input("Введіть частину світу, де розташована країна: ")
    area = int(input("Введіть площу країни: "))
    population = int(input("Введіть населення країни: "))
    countries[key] = Country(location, area, population)
    print("Країна ", key, " додана до словнику.")


def _del_country():
    key = input("Введіть країну, яку хочете видалити зі словника: ")
    if countries.get(key) is None:
        print("Такої країни нема у словнику.")
    else:
        del countries[key]
        print(key, "було видалено зі словника.")


def sort_countries():
    # sorted(countries) => sorted keys
    sorted_countries = {k: countries[k] for k in sorted(countries)}
    print("Відсортований словник: ")
    for key, value in sorted_countries.items():
        print_country(key, value)


def get_country_by_location(location):
    for key, value in countries.items():
        if value.location == location:
            print(key)


def task5():
    init_countries()
