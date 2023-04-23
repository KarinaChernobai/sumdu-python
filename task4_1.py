# Написати програму, в якій створити одновимірний масив та виконати над ним обчислення;
# Дано одномірний масив, що складається з N дійсних елементів.
# Масив користувач має ввести з клавіатури. Обчислити середнє арифметичне від’ємних елементів масиву.

def fn1():
    n = int(input("Enter array length: "))
    print(f"Enter {n} array items:")
    arr = [int(input()) for _ in range(n)]
    count = 0
    neg_sum = 0
    for num in arr:
        if num < 0:
            neg_sum += num
            count += 1
    if count > 0:
        print("Average for the negative numbers in the array: ", neg_sum / count)
    else:
        print("Average cannot be calculated.")


# Написати програму, в якій створити двовимірний масив з використанням циклів;
# Заповнити двовимірний масив розміром 7x7 таким чином, як показано на рисунку згідно з Вашим варіантом.
# Вивести масив на екран. Для виконання завдання використовуйте цикли.

def fn2():
    n = 7
    nums = []

    for i in range(0, n):
        num = i + 1
        intl = [0] * n
        for j in range(n-1, -1, -1):
            if num > 0:
                intl[j] = num
                num -= 1
            else:
                break
        nums.append(intl)

    for num in nums:
        print(*num)


def task4_1():
    fn1()
    fn2()
