# Написати програму для отримання зрізу рядка
# Запишіть у змінну довільний рядок в та отримайте з неї наступні зрізи,
# якщо довжина слова достатня для виконання операції зрізу.
# Отримати послідовність символів від 12-го символу по 15-й (15-й символ не включається).
def sub_sentc():
    sentc = str(input("Введіть рядок довжиною у 15 символів або більше: "))
    while len(sentc) < 15:
        sentc = str(input("Довжина рядка менше 15 символів. Введіть рядок ще раз: "))
    print("Послідовність символів від 12-го символу по 15-й(виключно):", sentc[11:14])
    # print("Послідовність символів від 12-го символу по 15-й:", sentc[slice(11, 14)]) -- another option


# Написати програму для обробки слів
# Задано слово, в якому є дві й більше однакові літери. Скласти програму, яка їх визначає і виводить на екран.
def analyze_word():
    word = str(input("Введіть слово, в якому є дві й більше однакові літери: ")).strip()
    while len(word) <= 1:
        word = str(input("Введіть слово, в якому є дві й більше однакові літери: ")).strip()
    word_dict = dict()
    for char in word:
        if word_dict.get(char) is None:
            word_dict[char] = 1
        else:
            word_dict[char] += 1
    for char, count in word_dict.items():
        if count > 1:
            print("Літера", char, "зустрічається", count, "разів")


# Написати програму для обробки рядків
# Задано речення. Скласти програму, яка визначає і виводить на екран кількість слів, які розпочинаються з літери «н».
def analyze_str():
    sentc = str(input("Введіть речення: ")).strip()
    while len(sentc) == 0:
        sentc = str(input("Введіть речення: ")).strip()
    sentc = sentc.lower()
    count = 0
    letter = "н"
    if sentc[0] == letter:
        end_i = sentc.find(" ", 1)
        print(sentc[0:end_i])
        count += 1
    for i in range(0, len(sentc)):
        if sentc[i] == letter and sentc[i - 1] == " ":
            end_i = sentc.find(" ", i + 1)
            print(sentc[i:end_i])
            count += 1
    print("Всього слів, які починаються з заданої літери:", count)


def task3():
    sub_sentc()
    analyze_word()
    analyze_str()
