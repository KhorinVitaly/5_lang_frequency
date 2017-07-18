import re
from collections import Counter
from sys import argv


def load_data(filepath):
    with open(filepath, "r") as file:
        return file.read()


def get_most_frequent_words(text, word_quantity):
    lower_text = text.lower()
    words = re.findall(r'(\w+)', lower_text, re.UNICODE)
    return Counter(words).most_common(word_quantity)


def fetch_text():
    try:
        filepath = argv[1]
        text = load_data(filepath)
        return text
    except FileNotFoundError:
        print("File not found!")
    except IndexError:
        print("File not specified!")
    exit()


def print_most_frequent_words(word_quantity):
    text = fetch_text()
    if not text:
        print("File is empty!")
        exit()
    most_frequent_words = get_most_frequent_words(text, word_quantity)
    print("The most frequent words in your text:")
    for word, count in most_frequent_words:
        print(word, count)


if __name__ == '__main__':
    word_quantity = 10
    print_most_frequent_words(word_quantity)

