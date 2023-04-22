# Реалізувати дві функції користувача в одній програмі.
# 1) z = 1/√(m+2)
# Число m вводиться користувачем у консолі Pyton.
# 2) Почавши тренування, спортсмен у перший день пробіг 10 км. Щодня він збільшував денну норму на 10% норми попереднього дня. Який сумарний шлях пробіжить спортсмен за n днів?
import math

def calculate(m: int):
    return 1 / math.sqrt(m + 2)

# n can only be positive
# арифметична прогресія
def solve(n: int):
    kms = 10
    kmsSum = kms
    for i in range(1, n):
        kms = kms + 0.1 * kms
        print(kms)
        kmsSum += kms
    print(kmsSum)

# S_n = n / 2 * (2 * a + (n - 1) * d),
def solve2(n: int):
    s = n / 2 * (2 * 10 + (n - 1) * 1)
    print(s)