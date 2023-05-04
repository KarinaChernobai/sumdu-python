import csv

field_names = ['Country Name', 'GDP per capita']
countries = []
target_year = "2016"
empty_value = "no data"

source_file = 'countries.csv'
res_file = 'picked_countries.csv'


def print_countries():
    print(f"This program prints GDP per capita for every country in {target_year}.")
    with open(source_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        cell_name_i = 0
        cell_val_i = 0
        for row in csv_reader:
            if line_count == 0:
                for i in range(0, len(row)):
                    cell = row[i]
                    if cell == field_names[0]:
                        cell_name_i = i
                    if cell == target_year:
                        cell_val_i = i
                line_count += 1
            else:
                country_name = row[cell_name_i]
                gdp = row[cell_val_i] if row[cell_val_i] != "" else empty_value
                print(f'{country_name}: {gdp}')
                countries.append({field_names[0]: country_name, field_names[1]: gdp})
                line_count += 1
        print(f'Processed {line_count} lines.')


def search_countries():
    gdp_limit = float(input("Search for countries with GDP greater than: "))
    picked_countries = []
    gdp = field_names[1]

    for country in countries:
        if country[gdp] != empty_value and gdp_limit < float(country[gdp]):
            picked_countries.append(country)

    with open(res_file, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(picked_countries)

    print(f'Search results were saved in {res_file}')


def task7_1():
    print_countries()
    search_countries()
