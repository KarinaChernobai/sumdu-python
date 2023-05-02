import string


def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
    except OSError:
        print("Could not open/read file:", file_name)
        return None
    else:
        print("File", file_name, "was opened.")
        return file


# створює текстовий файл TF4_1 із символьних рядків різної довжини,
# слова в яких розділені пробілами й розділовими знаками (слова не перевищують довжину 16 символів);
def create_txt_file(file_name):
    file = open_file(file_name, "w")
    if file is not None:
        file.write("Wild nights - Wild nights! Were I with thee, Wild nights should be,    Our luxury!")
        print("Information was successfully added to", file_name)
        file.close()
        print("File " + file_name + " was closed.")


# Читає вміст файлу TF4_1, визначає скільки в ньому є слів з одного, двох, трьох,
# і т. д. символів, результат записує у файл TF4_2:
# у перший рядок слово і кількість слів з одного символу,
# у другий рядок слово і кількість слів із двох символів і т. д.;
def analyze_data_from_file(file_name_1, file_name_2):
    file_1_r = open_file(file_name_1, "r")
    file_2_w = open_file(file_name_2, "w")
    if file_1_r is not None and file_2_w is not None:
        words_freq_dict = dict()
        file_str = file_1_r.read()
        file_str = file_str.translate(str.maketrans('', '', string.punctuation))
        for word in file_str.split(" "):
            word_len = len(word)
            if word_len == 0:  # to exclude empty strings
                continue
            word_freq = words_freq_dict.get(word_len)
            if word_freq is None:
                words_freq_dict[word_len] = 1
            else:
                words_freq_dict.update({word_len: word_freq + 1})

        for count, freq in sorted(words_freq_dict.items()):
            file_2_w.write(
                "Words with the char count of " + str(count) + " were found " + str(freq) + " time(s)." + '\n')

        file_1_r.close()
        file_2_w.close()
        print("Files were closed.")


# читає вміст файлу TF4_2 і друкує його по рядках.
def write_from_file_to_console(file_name):
    file = open_file(file_name, "r")
    if file is not None:
        print()
        for line in file.read().split('\n'):
            print(line)
        file.close()
        print("File " + file_name + " was closed.")


def task6():
    file_name_1 = "TF4_1.txt"
    file_name_2 = "TF4_2.txt"
    create_txt_file(file_name_1)
    analyze_data_from_file(file_name_1, file_name_2)
    write_from_file_to_console(file_name_2)
