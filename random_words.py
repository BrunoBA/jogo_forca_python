import random


def get_random_name():
    file = open("./files/words.txt", "r")
    file_lines = file.readlines()
    random_index = random.randrange(0, len(file_lines))

    return str(file_lines[random_index]).strip()
