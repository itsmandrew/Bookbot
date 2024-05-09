"""Module providing a function printing books"""
from collections import defaultdict

def main():
    """
    Main function for python script
    """

    with open("books/frankenstein.txt", encoding="utf-8") as file_book:
        file_contents = file_book.read()

    number_of_words = count_words(file_contents)
    letters_map = count_letters(file_contents)

    res = generate_report(number_of_words, letters_map)

    print(res)

def count_words(text):
    """
    Counts the number of words (separated by whitespace) in the given text file.

    Args:
        text (string): String of book given line by line

    Returns:
        int: The number of words in the given text file.
    """
    words = text.split()

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
        for letter in word.lower():
            hash_map[letter] += 1
    return hash_map

def generate_report(word_count, letter_map):
    """
    Generates a report of the total number of words and prints out the number 
    of occurences of each character.

    Args:
        word_count (int): number of words in the file
        letter_map (defaultdict): hash-map of the -> letters : occurences

    Returns:
        string: the report
    """

    res = "--- Begin report of books/frankenstein.txt ---\n"
    res += f"{word_count} words found in the document\n"

    list_of_dicts = []
    for key, num_val in letter_map.items():
        if key.isalpha():
            hash_map = {}
            hash_map['letter'] = key
            hash_map['nums'] = num_val
            list_of_dicts.append(hash_map)

    list_of_dicts.sort(reverse=True, key=lambda k: k['nums'])
    for hash_map in list_of_dicts:
        res += f"The \'{hash_map['letter']}\' character was found {hash_map['nums']} times\n"

    res += "--- End report ---"

    return res

if __name__ == "__main__":
    main()
