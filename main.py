import sys

from stats import get_letter_count, get_word_count, logic_sort


def get_book_text(path_to_file):
    """Open the file to read the contents"""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    try:
        # sys.argv[1] is the filepath to the book
        if sys.argv[1] is None:
            raise Exception
        book = get_book_text(sys.argv[1])
        word_count = get_word_count(book)
        letter_count = get_letter_count(book)
        organized_list = logic_sort(letter_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for item in organized_list:
            print(f"{item['char']}: {item['num']}")

    except Exception as e:
        print(f"Usage: python3 main.py <path_to_book> \nError: {e}")
        sys.exit(1)


main()
