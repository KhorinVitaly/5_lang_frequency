import re
from sys import argv
from operator import itemgetter


def load_data(filepath):
    with open(filepath, "r") as file:
        return file.read()

def get_most_frequent_words(text):
    words = re.findall(r'(\w+)', text, re.UNICODE)
    statistic = {}

    for word in words:
        statistic[word] = statistic.get(word, 0) + 1

    sorted_list = sorted(statistic.items(), key=itemgetter(1), reverse=True)
    return sorted_list[:10]


if __name__ == '__main__':
    text = load_data(argv[1])
    most_frequent_words = get_most_frequent_words(text)
    print("The most frequent words in your text:")
    for word, count in most_frequent_words:
        print(word, count) 