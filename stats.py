def get_word_count(text):
    book_list = text.split()
    word_count = len(book_list)
    return word_count


def get_letter_count(text):
    letter_list = list(text)
    dict_letter = {}

    for letter in letter_list:
        check_letter = letter.lower()
        if check_letter in dict_letter:
            dict_letter[check_letter] += 1
        else:
            dict_letter[check_letter] = 1

    return dict_letter


def logic_sort(items):
    word_dict_list = []

    for item in items:
        tmp_dict = {}
        if item.isalpha():
            tmp_dict["char"] = item
            tmp_dict["num"] = items[item]
            word_dict_list.append(tmp_dict)

    word_dict_list.sort(reverse=True, key=sort_on)

    return word_dict_list


def sort_on(item):
    return item["num"]
