import numpy as np


def init():
    print("Якщо ви хочете помножити дві матриці, тоді натисніть -> 1 <-")
    print("Якщо ви хочете транспонувати матрицю, тоді натисніть -> 2 <-")
    print("Якщо ви хочете знайти обернену матрицю, тоді натисніть  -> 3 <-")
    print("Якщо ви хочете знайти визначник матриці, тоді натисніть -> 4 <-")
    print("Якщо ви хочете вирішити систему лінійних рівнянь, тоді натисніть -> 5 <-")
    print("Якщо ви хочете знайти скалярний добуток векторів, тоді натисніть -> 6 <-")
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
                multiply_matrices()
            case 2:
                transpose_matrix()
            case 3:
                inverse_matrix()
            case 4:
                find_determinant()
            case 5:
                solve_linear_equation()
            case 6:
                dot_product()
            case _:
                raise Exception("You've entered the wrong code")
        print()
    return


def get_matrix_from_console():
    m = int(input("Введіть кількість рядків матриці А: "))
    n = int(input("Введіть стовпчиків матриці А: "))
    A = []
    for i in range(m):
        a = []
        for j in range(n):
            a.append(int(input(f"Введіть елемент [{i}][{j}] матриці A: ")))
        A.append(a)
    A = np.array(A)
    print("Матриця А")
    print(A)
    return A


def get_matrix_from_console_2(m, n, name):
    A = []
    for i in range(m):
        a = []
        for j in range(n):
            a.append(int(input(f"Введіть елемент [{i}][{j}] матриці {name}: ")))
        A.append(a)
    return np.array(A)


def multiply_matrices():
    m_1 = int(input("Введіть кількість рядків матриці А: "))
    n_1 = int(input("Введіть стовпчиків матриці А: "))
    m_2 = int(input("Введіть кількість рядків матриці B: "))
    n_2 = int(input("Введіть стовпчиків матриці B: "))
    if n_1 != m_2:
        print("Такі матриці неможливо помножити, "
              "так як кількість стовпчиків матриці А не дорівнює кількості рядків матриці В.")
        return
    A = get_matrix_from_console_2(m_1, n_1, "A")
    B = get_matrix_from_console_2(m_2, n_2, "B")
    C = A @ B  # preferred option

    print("Матриця А")
    print(A)
    print("Матриця В")
    print(B)
    print("Матриця C = A · B")
    print(C)
    return C


def transpose_matrix():
    A = get_matrix_from_console()
    print("Матриця A^T")
    AT = A.transpose()
    print(AT)
    return AT


def inverse_matrix():
    n = int(input("Введіть кількість рядків та стовпчиків матриці А: "))
    A = get_matrix_from_console_2(n, n, "A")
    A = np.linalg.inv(A)
    print("Матриця A^-1")
    print(A)
    return A


def find_determinant():
    n = int(input("Введіть кількість рядків та стовпчиків матриці А: "))
    A = get_matrix_from_console_2(n, n, "A")
    det = np.linalg.det(A)
    print("Визначник матриці А:", det)
    return det


# Використання бібліотеки NumPy для розв’язання задач лінійної алгебри.
# solves a system of linear equations
def solve_linear_equation():
    n = int(input("Кількість невідомих в системі: "))
    A = []
    B = []
    for i in range(n):
        b = []
        for j in range(n):
            num = int(input(f"Введіть x{j + 1} для рівняння {i + 1}: "))
            b.append(num)
        num = int(input(f"Введіть вільний член для рівняння {i + 1}: "))
        B.append(num)
        A.append(b)

    print("Основна матриця")
    print(A)
    print("Стовпчик вільних членів")
    print(B)
    X = np.linalg.solve(A, B)
    print("Розв'язок")
    print(X)
    return X


def dot_product():
    n = int(input("Введіть розмірність векторів: "))
    x = []
    y = []
    for i in range(n):
        x.append(int(input(f"Введіть координату {i+1} першого вектору: ")))
    for i in range(n):
        y.append(int(input(f"Введіть координату {i+1} другого вектору: ")))
    x = np.array(x)
    y = np.array(y)
    product = np.dot(x, y)
    print("Перший вектор")
    print(x)
    print("Другий вектор")
    print(y)
    print("Добруток векторів:", product)
    return product


def task10():
    init()
