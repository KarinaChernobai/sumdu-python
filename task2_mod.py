# Почавши тренування, спортсмен у перший день пробіг 10 км.
# Щодня він збільшував денну норму на 10% норми попереднього дня.
# Який сумарний шлях пробіжить спортсмен за n днів?
def solve2(n: int):
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
