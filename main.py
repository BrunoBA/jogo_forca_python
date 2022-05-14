
from random_words import get_random_name
import outputs
from my_strings import change_word_to_underline, check_if_exists_on_word, show_correct_letters, parse_input

outputs.game_start()
word = get_random_name()


win = False
dead = False
lifes = 10
tried_letters = []

while(not win and not dead):
    if (len(tried_letters) > 0):
        outputs.show_values(lifes, tried_letters, string_with_underline)
    else:
        string_with_underline = change_word_to_underline(word)
        print(string_with_underline)
        print("\n")

    letter = input("Escolha uma letra: ")
    letter = parse_input(letter)

    if(len(letter) == 0):
        continue

    exists = check_if_exists_on_word(word, letter)

    if(letter not in tried_letters):
        tried_letters.append(letter)
    else:
        exists = False

    if(exists):
        string_with_underline = show_correct_letters(word, tried_letters)
    else:
        lifes -= 1

    if (string_with_underline.replace(" ", "") == word):
        win = True

    if(lifes == 0):
        dead = True

if (win):
    outputs.winner()

if(dead):
    outputs.game_over()

outputs.reveal_the_word(word)
