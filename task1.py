# Написати програму обчислення математичного виразу із застосуванням умовних операторів
# числа a та b можуть бути лише додатними. Реалізувати у програмі перевірку чисел a та b, введених користувачем
def compare():
    a = int(input("Enter a = "))
    while a <= 0:
        a = int(input("a must be a positive integer. Enter a = "))
    b = int(input("Enter b = "))
    while b <= 0:
        b = int(input("b must be a positive integer. Enter b = "))
    if a < b:
        print("b is greater than a")
        res = a / b + 5
    elif a == b:
        print("a and b are equal")
        res = -5
    else:
        print("a is greater than b")
        res = (a * a - b) / b
    print("Result: ", res)
    print()
    return res


# написати програму із застосуванням циклічних алгоритмів
# Знайти та надрукувати перші 8 чисел з ряду Фібоначчі та їх суму.
def fibonacci(limit: int):
    if limit <= 0:
        raise Exception("Only positive integers are allowed")
    elif limit == 1:
        print("1. 1")  # special case
    f_seq = [1, 1]
    f_sum = 2
    print("1. 1")
    print("2. 1")
    for i in range(2, limit):
        f_num = f_seq[i - 1] + f_seq[i - 2]
        print("%i. %i" % (i + 1, f_num))
        f_seq.append(f_num)
        f_sum += f_num
    print("f_sum:", f_sum)
    print()


# написати програму побудови піраміди із використанням циклу for
# Вводиться ціле число N (1<N<9), а виводяться рядки з числами, які утворюють визначений «рисунок».
def draw_pyramid(n: int):
    if n <= 1 or n >= 9:
        raise Exception("N must be greater than 1 and less than 9.")
    for x in range(0, n):
        for y in range(0, x + 1):
            print(y + 1, end=" ")
        print()
    print()


def task1():
    compare()
    fibonacci(8)
    draw_pyramid(8)
