import unicodedata


def change_word_to_underline(word):
    new_word = ""
    for _ in word:
        new_word += " _"

    return new_word


def remove_special_characters(word):
    text = unicodedata.normalize('NFD', word)\
        .encode('ascii', 'ignore')\
        .decode("utf-8")

    return str(text).lower().strip()


def check_if_exists_on_word(word, letter):
    letter = remove_special_characters(letter)
    word = remove_special_characters(word)

    return word.find(letter) != -1


def show_correct_letters(word, tries):
    new_word = ""
    for l in word:
        without_accents = remove_special_characters(l)
        if(without_accents in tries):
            new_word += " " + l
        else:
            new_word += " _"

    return new_word


def parse_input(input):
    if(len(input) > 1):
        input = input[0]

    return remove_special_characters(str(input))
