import json

countries = dict()
file_name = 'countries.json'


def init_countries():
    load_JSON(file_name)

    print("Якщо ви хочете вивести усі значення з JSON файлу, тоді натисніть -> 1 <-")
    print("Якщо ви хочете додати новий запис до JSON файлу, тоді натисніть -> 2 <-")
    print("Якщо ви хочете видалити запис з JSON файлу, тоді натисніть -> 3 <-")
    print("Якщо ви хочете переглянути вміст словника за відсортованими ключами, тоді натисніть -> 4 <-")
    print("Якщо ви хочете дізнатися чи є серед заданих країн ті, що знаходяться в Африці, тоді натисніть -> 5 <-")
    print("Якщо ви хочете дізнатися чи є серед заданих країн ті, що знаходяться в Азії, тоді натисніть -> 6 <-")
    print("Якщо ви хочете знайти країну за обраним полем -> 7 <-")
    print("Якщо ви хочете вийти з програми, тоді натисніть -> 0 <-")
    while True:
        action = int(input("Введіть пункт меню: "))
        if action < 0 or action > 7:
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
                del_country()
            case 4:
                sort_countries()
            case 5:
                get_country_by_location("Africa")
            case 6:
                get_country_by_location("Asia")
            case 7:
                get_country_by_field()
            case _:
                raise Exception("You've entered the wrong code")
        print()


# load_JSON is changed for task8
def load_JSON(file_name):
    global countries
    file = open(file_name)
    countries = json.load(file)
    file.close()
    return countries


def update_JSON():
    json_object = json.dumps(countries, indent=4)
    with open("countries.json", "w") as outfile:
        outfile.write(json_object)


def print_countries():
    for key, value in countries.items():
        print_country(key, value)


def print_country(key, value):
    print('\033[1m', key, '\033[0m')
    print("частина світу:", value['location'])
    print("площа:", value['area'])
    print("населення:", value['population'])
    print()


def add_country():
    key = input("Введіть країну, яку хочете додати до JSON файлу: ")
    location = input("Введіть частину світу, де розташована країна: ")
    area = int(input("Введіть площу країни: "))
    population = int(input("Введіть населення країни: "))
    countries[key] = {'location': location, 'area': area, 'population': population}
    update_JSON()
    print("Країна ", key, " додана до JSON файлу.")


def del_country():
    key = input("Введіть країну, яку хочете видалити з файлу: ")
    if countries.get(key) is None:
        print("Такої країни нема у JSON файлі.")
    else:
        del countries[key]
        update_JSON()
        print(key, "було видалено з JSON файлу.")


def sort_countries():
    # sorted(countries) => sorted keys
    sorted_countries = {k: countries[k] for k in sorted(countries)}
    print("Відсортований словник: ")
    for key, value in sorted_countries.items():
        print_country(key, value)


def get_country_by_location(location):
    for key, value in countries.items():
        if value['location'] == location:
            print(key)


def get_country_by_field():
    t_key = input("Введіть поле за яким буде проходить пошук (location, area, population): ")
    if t_key == 'area' or t_key == 'population':
        t_value = int(input("Введіть значення поля: "))
    elif t_key == 'location':
        t_value = input("Введіть значення поля: ")
    else:
        print("Ви ввели поле, якого не існує.")
        return
    found = False
    for key, value in countries.items():
        if value[t_key] == t_value:
            print(key)
            found = True
    if not found:
        print("Країну за даним полем не було знайдено.")


def task7_2():
    init_countries()
