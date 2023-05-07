import string
import re
import pandas as pd
import matplotlib.pyplot as plt
from nltk import FreqDist
from nltk.corpus import gutenberg, stopwords
from datetime import datetime
from task7_2 import load_JSON

file_name_json = 'countries.json'


# groups data about countries by location and finds the sum of the population in each group.
def analyze_countries_data():
    countries_json = load_JSON(file_name_json)
    df = pd.DataFrame(countries_json)
    df = df.transpose()
    df = df.reset_index()
    df.columns = ['country', 'location', 'area', 'population']
    print(df.to_string())
    print()

    sum_df = df.groupby('location').population.agg('sum')
    sum_df = sum_df.reset_index()
    sum_df.columns = ['location', 'population sum']
    print(sum_df.to_string())


# Створіть датафрейм з даними використання велодоріжок за рік.
# Визначте, який місяць найбільш популярний у велосипедистів.
def analyze_cycling_data():
    df = pd.read_csv('comptage_velo_2018.csv')

    df["day sum"] = df.sum(axis=1, numeric_only=True)

    months_data_set = {
        'month': ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"
                  ],
        'sum': [0] * 12
    }

    for ind in df.index:
        date_time_str = df['Date'][ind]
        date_time_obj = datetime.strptime(date_time_str, '%d/%m/%Y')
        month = date_time_obj.strftime("%m")
        months_data_set["sum"][int(month) - 1] += df['day sum'][ind]

    months_df = pd.DataFrame(months_data_set)
    print("The sum of the cyclists on tracks for each month:")
    print(months_df)
    print()

    print("The most popular month for the cyclists:")
    print(months_df[months_df['sum'] == months_df['sum'].max()])


def analyze_book_text():
    sense_words = gutenberg.words('austen-sense.txt')
    print("Word count:", len(sense_words))

    f_dist = FreqDist(sense_words)
    data = f_dist.most_common(10)
    x = [data[el][0] for el in range(len(data))]
    y = [data[el][1] for el in range(len(data))]
    plt.bar(x, y)
    plt.title("10 найбільш вживаних слів у тексті")
    plt.xlabel("Слова")
    plt.ylabel("Зустрічаються разів у тексті")
    plt.show()

    mod_sense_words = [x for x in sense_words if not re.fullmatch('[' + string.punctuation + ']+', x)]
    stop_words = set(stopwords.words("english"))
    mod_sense_words = [word for word in mod_sense_words if word not in stop_words]

    f_dist = FreqDist(mod_sense_words)
    data = f_dist.most_common(10)
    x = [data[el][0] for el in range(len(data))]
    y = [data[el][1] for el in range(len(data))]
    plt.bar(x, y)
    plt.title("10 найбільш вживаних слів у тексті")
    plt.xlabel("Слова")
    plt.ylabel("Зустрічаються разів у тексті")
    plt.show()


def task9():
    analyze_countries_data()
    analyze_cycling_data()
    analyze_book_text()
