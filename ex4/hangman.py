#############################################################################################
# FILE : hangman.py
# WRITERS : ElinorB
# EXERCISE : Intro2cs ex4 
# DESCRIPTION : Hangman game
#############################################################################################

import hangman_helper
import string

NUM_LETTERS = 26
CHAR_A = 97


def update_word_pattern(word, pattern, letter):
    """Function meant to receive: a word, the pattern of the word and a single letter.
    if the letter shows in the given word then the function will return an updated pattern which contains
    the given letter in the matching location."""

    for i in range(len(word)):
        if letter == word[i]:
            pattern = pattern[:i] + letter + pattern[i+1:]
    return pattern


def run_single_game(words_list):
    """Function is meant to receive a list of words and run the game."""

    word = hangman_helper.get_random_word(words_list)
    word_length = len(word)
    wrong_guess_lst = []
    error_count = 0
    pattern = '_' * word_length
    msg = hangman_helper.DEFAULT_MSG

    while pattern != word and error_count < hangman_helper.MAX_ERRORS:

            hangman_helper.display_state(pattern, error_count, wrong_guess_lst, msg)
            user_input = hangman_helper.get_input()

            if user_input[0] == hangman_helper.HINT:
                good_words = filter_words_list(words_list, pattern, wrong_guess_lst)
                hint_letter = choose_letter(good_words, pattern)
                msg = hangman_helper.HINT_MSG + hint_letter
                hangman_helper.display_state(pattern, error_count, wrong_guess_lst, msg)

            if user_input[0] == hangman_helper.LETTER:
                letter = user_input[1]

                if letter not in list(string.ascii_lowercase):   # Uses an imported file, 'list(string.ascii_lowercase)' is a list of the lowercase english alphabet.
                    msg = hangman_helper.NON_VALID_MSG

                elif letter in pattern or letter in wrong_guess_lst:
                    msg = hangman_helper.ALREADY_CHOSEN_MSG + letter

                elif letter in word:
                    pattern = update_word_pattern(word, pattern, letter)
                    msg = hangman_helper.DEFAULT_MSG

                else:
                    wrong_guess_lst.append(letter)
                    error_count += 1
                    msg = hangman_helper.DEFAULT_MSG

    if pattern == word:
        msg = hangman_helper.WIN_MSG
        hangman_helper.display_state(pattern, error_count, wrong_guess_lst, msg, True)
    else:
        msg = hangman_helper.LOSS_MSG + word
        hangman_helper.display_state(pattern, error_count, wrong_guess_lst, msg, True)


def filter_words_list(words, pattern, wrong_guess_lst):
    """

    :param words: A list of words
    :param pattern: an updated pattern
    :param wrong_guess_lst: A list of wrong guesses of letters
    :return: A list of 'good words'
    """
    """Function is meant to receive a list of words, a list of wrong guesses, and a specific pattern and return
       an updated list containing the words that:1. whom length is the same as the patten length. 2. have the same
        letters appearing in the correct location as in the pattern. 3. don't have any of the 'wrong letter guess 
        list' letters appearing in them."""

    good_words = []

    for word in words:
        if len(pattern) != len(word):
            continue

        is_good = True
        for i in range(len(word)):

            if pattern[i] != '_' and word[i] != pattern[i]:
                is_good = False
            if word[i] in wrong_guess_lst:
                is_good = False

        if is_good:
            good_words.append(word)

    return good_words


def choose_letter(words, pattern):
    """Function is meant to receive a filtered list of words and the current pattern,
        and return a letter that doesn't show in the pattern and shows the most in the
        filtered list."""

    count_list = [0] * NUM_LETTERS

    for word in words:
        for letter in word:
            index = letter_to_index(letter)
            count_list[index] += 1

    max_index = 0
    max_count = 0
    for i in range(NUM_LETTERS):
        if count_list[i] > max_count and index_to_letter(i) not in pattern:
            max_count = count_list[i]
            max_index = i

    return index_to_letter(max_index)


def letter_to_index(letter):

    return ord(letter.lower()) - CHAR_A


def index_to_letter(index):

    return chr(index+CHAR_A)


def main():
    words_list = hangman_helper.load_words()
    while True:
        run_single_game(words_list)
        if hangman_helper.get_input() == (hangman_helper.PLAY_AGAIN, False):
            break


if __name__ == "__main__":
    hangman_helper.start_gui_and_call_main(main)
    hangman_helper.close_gui()











