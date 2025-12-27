from operator import le

from stats import get_letter_count, get_word_count, logic_sort


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book)
    letter_count = get_letter_count(book)
    organized_list = logic_sort(letter_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in organized_list:
        print(f"{item['char']}: {item['num']}")


main()
