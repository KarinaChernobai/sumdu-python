import csv
import math
import matplotlib.pyplot as plt
import numpy as np

from task7_2 import load_JSON

file_name_json = 'countries2.json'
file_name_csv = 'countries_labor_force.csv'

field_names = ['Country Name', "Country Code", "Series", "Series Code"]
countries = []
x_years = []


# Побудуйте графік функції.
# Оберіть суцільний тип лінії, задайте колір та товщину графіку та позначте осі,
# виведіть назву графіка на екран, вставте легенду.
# Y(x)=2^x*sin(10x), x=[-3...3]
def draw_func_graph():
    x_values = []
    y_value = []
    for x in range(-3, 4):
        x_values.append(x)
        y = 2 ** x * math.sin(10 * x)
        y_value.append(y)
    x_points = np.array(x_values)
    y_points = np.array(y_value)
    plt.plot(x_points, y_points, label='2^x*sin(10x)', color="red")
    plt.title('Function graph', fontsize=15)
    plt.xlabel('x', fontsize=12, color='blue')
    plt.ylabel('y', fontsize=12, color='blue')
    plt.legend()
    plt.grid(True)
    plt.show()


# 2.1. На одній координатній осі побудуйте графіки, що показують динаміку показника для двох країн,
# підпишіть осі –  по осі Х має відображатися рік, а по осі Y має відображатися значення показника.
# 2.2 Побудуйте стовпчасті діаграми, які відображатимуть значення показника для кожної з країн.
# Назву країни для побудови діаграми має вводити користувач з клавіатури.
def draw_graphs_from_data():
    draw_diagram()
    draw_bar_chart()


# reads csv file and draws a chart for two countries
def draw_diagram():
    global x_years
    y_labor = []
    z_labor = []
    with open(file_name_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        counter = 0
        start = len(field_names)
        for row in csv_reader:
            if counter == 0:
                for i in range(start, len(row)):
                    x_years.append(int(row[i][0:5]))
                counter += 1
            else:
                countries.append(row)  # for draw_bar_chart fn
            country_name = row[0]
            if country_name == "Ukraine":
                for i in range(start, len(row)):
                    y_labor.append(int(row[i]))
            if country_name == "United States":
                for i in range(start, len(row)):
                    z_labor.append(int(row[i]))
    np.array(x_years)
    np.array(y_labor)
    np.array(z_labor)
    plt.plot(x_years, y_labor, label='Ukraine', color="blue")
    plt.plot(x_years, z_labor, label='United States', color="red")
    plt.title('Labor force, total', fontsize=15)
    plt.xlabel('Year', fontsize=12, color='green')
    plt.ylabel('Value', fontsize=12, color='green')
    plt.legend()
    plt.grid(True)
    plt.show()


# lets user pick a country and then draws a bar chart.
def draw_bar_chart():
    country_name = input("Select country for the bar chart: ")
    data2 = dict()
    for country in countries:
        if country_name == country[0]:
            i = 0
            for j in range(len(field_names), len(country)):
                year = x_years[i]
                data2[year] = country[j]
                i += 1
    x_values = list(data2.keys())
    y_values = list(data2.values())
    plt.bar(x_values, y_values, color='maroon', width=0.4)
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.title("Labor force, total")
    plt.show()


# Побудуйте кругову діаграму на основі даних з предметної області
def draw_pie_chart():
    countries_locations = dict()
    countries_json = load_JSON(file_name_json)
    for value in countries_json.values():
        location = value['location']
        if countries_locations.get(location) is None:
            countries_locations[location] = 1
        else:
            countries_locations[location] += 1
    x = []
    y = []
    for key, value in countries_locations.items():
        x.append(key)
        y.append(value)
    np.array(x)
    np.array(y)
    fig, ax = plt.subplots()
    ax.pie(y, labels=x)
    ax.axis("equal")
    plt.legend()
    plt.show()


def task8():
    draw_func_graph()
    draw_graphs_from_data()
    draw_pie_chart()
