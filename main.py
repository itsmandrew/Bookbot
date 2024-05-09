"""Module providing a function printing books"""
from collections import defaultdict

def main():
    """
    Main function for python script
    """

    with open("books/frankenstein.txt", encoding="utf-8") as file_book:
        file_contents = file_book.read()

    print(file_contents)




def count_words(text):
    """
    Counts the number of words (separated by whitespace) in the given text file.

    Args:
        text (string): String of book given line by line

    Returns:
        int: The number of words in the given text file.
    """
    words = text.split()

    print(len(words))

    return len(words)

def count_letters(text):
    """
    Counts the number of letters in the given text file

    Args:
        text (string): String of book given line by line

    Returns:
        defaultdict: mapping from -> letter : occurrence
    """
    hash_map = defaultdict(int)
    words = text.split()

    for word in words:
        for letter in word:
            hash_map[letter] += 1
    print(hash_map)
    return hash_map


if __name__ == "__main__":
    main()
