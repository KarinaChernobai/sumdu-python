# Реалізувати функцію, яка виконує операції над списками –
# вставку елемента в список у вказану позицію
# та друк списку на екран.
# Список користувач має вводити з клавіатури.
def modify_list():
    num_list = list(map(int, input('Enter a list of integers: ').split()))
    print(num_list)
    item = int(input('Enter a new item: '))
    i = int(input('Enter the index at which the new item will be placed: '))
    num_list.insert(i, item)
    print(num_list)
    return num_list


# Реалізувати функцію, яка виконує операції над списками –
# пошук послідовності елементів
# та друк списку на екран.
def find_sub_list():
    test_list = list(map(int, input('Enter a list of integers (separate items by comma): ').split(', ')))
    print(test_list)

    sub_list = list(map(int, input('Enter a sublist of integers (separate items by comma): ').split(', ')))
    print(sub_list)

    res = False
    for i in range(len(test_list) - len(sub_list) + 1):
        if test_list[i: i + len(sub_list)] == sub_list:  # slicing from i to i + sublist len
            res = True
            break

    print("Is the sublist present in the list? " + ("Yes." if res else "No."))


# Задано текст з цифр і літер латинського алфавіту.
# Скласти програму, яка визначає, яких літер –
# голосних {a, e, i, o, u, y} або приголосних більше в цьому тексті.
def count_letters():
    all_vowels = set('aeiouyY')
    all_consonants = set('bcdfghjklmnpqrstvwxz')
    text = set(input("Enter a text: ").lower())

    consonants = text & all_consonants
    cons_len = len(consonants)
    print("Consonants found: ", consonants)
    print(cons_len, "unique consonants found.")

    vowels = all_vowels & text
    vowl_len = len(vowels)
    print("Vowels found: ", vowels)
    print(vowl_len, "unique vowels found.")

    if cons_len > vowl_len:
        print("More unique consonants were found in this text.")
    elif cons_len < vowl_len:
        print("More unique vowels were found in the given text.")
    else:
        print("The numbers of unique consonants and vowels are equal.")


def task4_2():
    modify_list()
    find_sub_list()
    count_letters()
