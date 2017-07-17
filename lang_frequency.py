import re
import collections
from sys import argv


def load_data(filepath):
    try:
        with open(filepath, "r") as file:
            return file.read()
    except FileNotFoundError:
        return None


def get_most_frequent_words(text):
    lower_text = text.lower()
    words = re.findall(r'(\w+)', lower_text, re.UNICODE)
    statistic = collections.Counter()
    word_quantity_in_top = 10

    for word in words:
        statistic[word] += 1

    return statistic.most_common(word_quantity_in_top)


if __name__ == '__main__':
    try:
        text = load_data(argv[1])
    except IndexError:
        print("File not specified!")
        exit()

    if text:
        most_frequent_words = get_most_frequent_words(text)
        print("The most frequent words in your text:")
        for word, count in most_frequent_words:
            print(word, count)
    else:
        print("Text file is empty")