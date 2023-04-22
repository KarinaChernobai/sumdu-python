import math
from task2_mod import solve2


# Реалізувати дві функції користувача в одній програмі.


# z = 1/√(m+2)
# Число m вводиться користувачем у консолі Pyton.
def calculate():
    m = int(input("Enter m = "))
    divisor = math.sqrt(m + 2)
    if divisor == 0:
        print("Division by zero. The result is undefined.")
        return None
    z = 1 / divisor
    print(z)
    return z

# Почавши тренування, спортсмен у перший день пробіг 10 км.
# Щодня він збільшував денну норму на 10% норми попереднього дня.
# Який сумарний шлях пробіжить спортсмен за n днів?
def solve(n: int):
    if n == 1:
        print(10)
        return
    kms = 10
    print(kms)
    kms_sum = kms
    for i in range(1, n):
        kms = round(kms + 0.1 * kms)  # round is used to imitate the real world calculations
        print(kms)
        kms_sum += kms
    print("kms_sum", kms_sum)


def task2():
    calculate()
    solve(4)
    # Реалізувати функцію 2 із завдання 1 у вигляді окремого модуля,
    # підключити її в основну програму і продемонструвати роботу з нею.
    solve2(6)
