import csv
import os


def read_from_file():
    with open('example.csv', newline='') as File:
        reader = csv.reader(File)

        for row in reader:
            print(row)


def write_to_file():
    my_data = [["first_name", "second_name", "Grade"], ['Alex', 'Brian', 'A'], ['Tom', 'Smith', 'B']]
    my_file = open('example2.csv', 'w')
    with my_file:
        writer = csv.writer(my_file)
        writer.writerows(my_data)
    print("Writing complete")


def example2():
    with open('task7_1.data.csv', newline='') as File:
        reader = csv.reader(File)

        for row in reader:
            print(row)


def example():
    flag = False

    try:

        csvfile = open("Lab8.csv", "r")

        reader = csv.DictReader(csvfile, delimiter=";")

        print("Country Name: 2016 [YR2016]")

        for row in reader:
            print(row['Country Name'], ': ', row["2016 [YR2016]"])

        csvfile.close

    except:

        print("Файл Lab8.csv не знайдено!")

    try:

        csvfile = open("Lab8.csv", "r")

        reader = csv.DictReader(csvfile, delimiter=";")

        indicator = input("\nВведіть будь-яке значення, щоб знайти показники, які більші, ніж значення, яке ви ввели: ")

        while indicator.isalpha():
            indicator = input("Введіть значення ще раз, так як повина бути цифра: ")

        os.system('clear')

        print("Country Name: 2016 [YR2016]")

        for row in reader:

            if indicator < row["2016 [YR2016]"]:
                flag = True

                print(row["Country Name"], ": ", row["2016 [YR2016]"])

                with open("new_lab8.csv", "a") as csvfile2:
                    writer = csv.writer(csvfile2, delimiter=";")

                    writer.writerow((row["Country Name"], row["2016 [YR2016]"]))

        csvfile.close

        if flag == False:
            os.system('clear')

            print("Показників, які більші, ніж значення, яке ви ввели (" + indicator + ") - немає.")

    except:

        print("Файл Lab8.csv не знайдено!")


def task7_1():
    # example()
    # example2()
    read_from_file()
    write_to_file()
