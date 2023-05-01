######################################################################################################
# FILE : crossword3d.py
# WRITERS : ElinorB, ReutB
# EXERCISE : Intro2cs ex5
# DESCRIPTION : Crossword through a matrix
######################################################################################################


import os
import sys


NUM_PARAM = 5
WORDS_PARAM_NUM = 1
MATX_PARAM_NUM = 2
OUTPUT_PARAM_NUM = 3
DIRECTIONS_PARAM = 4
VALID_DIRECTION = "udrlwxyz"

ERROR_PARAMETERS = "ERROR: invalid number of parameters. Please enter word_file matrix_file output_file directions"
ERROR_WORDS_FILE_NOT_EXIST = ["ERROR: Word file ", " does not exist"]
ERROR_FOR_MATX_NOT_EXIST = ["ERROR: Matrix file "," does not exist"]
ERROR_DIRECTIONS = "ERROR: invalid directions"


def main(args):
    """
        Function is meant to receive arguments from user and check if all needed arguments are there and valid.
        If arguments are missing or not valid, the function will print specific error messages.
        Otherwise, the function will import the files given as arguments and organise the information in the files
        as ordered lists.
        The function will then run the main operation of the program using other functions.

        :param args: Input from user (via command line)
        """
    if len(args) != NUM_PARAM:
        print(ERROR_PARAMETERS)
        return None

    elif os.path.isfile(args[WORDS_PARAM_NUM]) == 0 \
            or (os.path.isfile(args[WORDS_PARAM_NUM]) == 0 and os.path.isfile(args[MATX_PARAM_NUM]) == 0):
        print(ERROR_WORDS_FILE_NOT_EXIST[0] + args[WORDS_PARAM_NUM] + ERROR_WORDS_FILE_NOT_EXIST[1])
        return None

    elif os.path.isfile(args[MATX_PARAM_NUM]) == 0:
        print(ERROR_FOR_MATX_NOT_EXIST[0] + args[MATX_PARAM_NUM] + ERROR_FOR_MATX_NOT_EXIST[1])
        return None

    elif sys.argv[DIRECTIONS_PARAM] == '' or valid_directions_check(args[DIRECTIONS_PARAM]) is False:
        print(ERROR_DIRECTIONS)
        return None

    else:
        original_word_list = open(args[WORDS_PARAM_NUM], 'r')

        original_matx = open(args[MATX_PARAM_NUM], 'r')

        output_file = open(args[OUTPUT_PARAM_NUM], 'w')

        directions = set(args[DIRECTIONS_PARAM])

        final_output = run_crossword(original_word_list, original_matx, output_file, directions)
        original_word_list.close()
        original_matx.close()
        return final_output


def run_crossword(original_word_list, original_matx, output_file, directions):
    """
    run the program to search words in given matrix and returns the words that was founded w/ num of founds
    in matrix according to given directions
    :param original_word_list:list of all words to search in matrix in lower-cases letters
    :param original_matx: lower-cases letters matrix
    :param output_file: txt file
    :param directions: string of valid directions
    :return: new output.txt file with list of words found and times they were founded organized in alpha-bet order.
    """
    all_word_list = original_word_list.readlines()  # the words as written in the original text
    word_list = [word.replace('\n', '') for word in all_word_list]  # the words in lower cases
    all_word_list_low = [letter.lower() for letter in word_list]

    all_matrix = original_matx.readlines()  # the lines of the matrix as written in the original text
    all_matrix_low = [letter.lower() for letter in all_matrix]

    if all_word_list == [] or all_matrix == []:
        return output_file.write('')

    str_list_to_check = []  # list w/ all the strings of lines/columns/diagonals require by directions

    for single_direction in directions:
        if single_direction == 'u':
            str_list_to_check.append(mirror_all_lines_lst(divide_to_columns(all_matrix_low)))
            continue
        elif single_direction == 'd':
            str_list_to_check.append(divide_to_columns(all_matrix_low))
            continue
        elif single_direction == 'r':
            str_list_to_check.append(divide_to_lines(all_matrix_low))
            continue
        elif single_direction == 'l':
            str_list_to_check.append(mirror_all_lines_lst(divide_to_lines(all_matrix_low)))
            continue
        elif single_direction == 'w':
            str_list_to_check.append(mirror_all_lines_lst(divide_to_diagonal_d_to_l(all_matrix_low)))
            continue
        elif single_direction == 'x':
            str_list_to_check.append(mirror_all_lines_lst(divide_to_diagonal_d_to_r(all_matrix_low)))
            continue
        elif single_direction == 'y':
            str_list_to_check.append(divide_to_diagonal_d_to_r(all_matrix_low))
            continue
        elif single_direction == 'z':
            str_list_to_check.append(divide_to_diagonal_d_to_l(all_matrix_low))
            continue

    crossword_output = histogram(sum(str_list_to_check, []), all_word_list_low, output_file)
    return crossword_output


def valid_directions_check(string):
    """
    check whether the directions inserted in sys were valid
    :param string = sys.argv[DIRECTION_PARAM]
    :return: False if the directions are not valid.
    """
    for letter in string:
        if letter not in VALID_DIRECTION:
            return False


def divide_to_lines(all_matrix_low):
    """
    A function meant to receive a list of letters derived from a matrix and return
    a list organized as lines w/o commas
    :param all_matrix_low: the matrix w/ lower case
    :return: The matrix organized as lines
    """

    line_list = [[] for i in range(len(all_matrix_low))]
    for index, line in enumerate(all_matrix_low):
        for letter in line:
            if letter == '\n':
                break
            if letter != ',':
                line_list[index].append(letter)
    return line_list


def mirror_line(line_string):
    """
    function that reverse the given string
    :param line_string: string
    :return: revered string
    """
    mirror_string = line_string[::-1]
    return mirror_string


def mirror_lines_matrix(all_matrix_low):
    """
    reverse all matrix lines
    :param all_matrix_low: the matrix w/ lower case
    :return: mirrored matrix's lines
    """
    matrix_lines = divide_to_lines(all_matrix_low)
    mirrored_lines = mirror_all_lines_lst(matrix_lines)
    return mirrored_lines


def mirror_all_lines_lst(list_of_lines):
    """
    reverse all given line in line list
    :param list_of_lines: list of lists of strings
    :return: mirrored lines list
    """
    mirrored_matx_lines = []

    for line in list_of_lines:
        the_mirror_line = mirror_line(line)
        mirrored_matx_lines.append(the_mirror_line)
    return mirrored_matx_lines


def divide_to_columns(all_matrix_low):
    """
    A function meant to receive a list of letters derived from a matrix and return
    a list organized as columns
    :param all_matrix_low: A list of letters without commas
    :return: The list organized as columns
    """
    columns_list = []
    column = []
    num_of_columns = len(divide_to_lines(all_matrix_low)[0])
    line_list = divide_to_lines(all_matrix_low)

    for i in range(num_of_columns):
        for line in line_list:
            column.append(line[i])
        columns_list.append(column)
        column = []

    return columns_list


def upside_down_matrix(all_matrix_low):
    """
    reverse all matrix columns
    :param all_matrix_low: the matrix w/ lower case
    :return: upside down matrix's line list
    """
    matrix_columns = divide_to_columns(all_matrix_low)
    upside_down_lines = mirror_all_lines_lst(matrix_columns)
    return upside_down_lines


def divide_to_diagonal_d_to_l(all_matrix_low):
    """
    A function meant to receive a list of letters derived from a matrix and return
    a list organized as up to down left lists (start from north-west corner)
    :param all_matrix_low
    :return: The list organized as down to left lines
    """
    num_of_columns = len(divide_to_lines(all_matrix_low)[0])
    num_of_lines = len(divide_to_columns(all_matrix_low)[0])
    diagonal_list_d_to_l = [[] for i in range(num_of_columns + num_of_lines - 1)]

    for y in range(num_of_lines):
        for x in range(num_of_columns):
            diagonal_list_d_to_l[y + x].append(divide_to_lines(all_matrix_low)[y][x])
    return diagonal_list_d_to_l


def divide_to_diagonal_d_to_r(all_matrix_low):
    """
    A function meant to receive a list of letters derived from a matrix and return
    a list organized as up to down right lists (start from north-east corner)
    :param all_matrix_low
    :return: The list organized as down to right lines
    """
    the_mirrored_matrix = mirror_lines_matrix(all_matrix_low)
    return divide_to_diagonal_d_to_l(the_mirrored_matrix)


def lst_to_concat_line_lst(list_of_lines):
    """
    A function that receives a list of lists of non concatenated letters
    and returns a list of concatenated lists.
    :param list_of_lines: List of lines of letters
    :return: A list of lists of concatenated strings
    """
    concat_line_list = []
    string = ""
    for i in list_of_lines:
        for letter in i:
            string = string + letter
        concat_line_list.append(string)
        string = ""
    return concat_line_list


def histogram(list_of_lines, word_list_low, output_file):
    """
    A function meant to receive a list of lists representing the lines\
    diagonals in a given matrix and a list of words. The function returns a
    an alphabetically ordered list representing the words from the list
    of words that appear in the given lines,
    and how many times each word appeared.

    :param output_file: txt file to write results on
    :param list_of_lines: list of strings lines to check
    :param word_list_low: A list of words
    :return: An alphabetically ordered list of the words from the list
    that appear in the matrix, and how many times each appeared.
    """

    output = dict()
    sorted_dict = []
    concatenated_line_list = lst_to_concat_line_lst(list_of_lines)

    for index, line in enumerate(concatenated_line_list):
        line_length = len(concatenated_line_list[index])
        # get the length of the specific line
        for word in word_list_low:
            if word not in line:
                continue
            for i in range(line_length):
                if line[i:i + len(word)] != word:
                    continue
                if word not in output:
                    output[word] = 1
                else:
                    output[word] += 1

    for key in sorted(output):
        new_val = ''.join([str(key), ',', str(output[key])])
        sorted_dict.append(new_val)
    output_file.writelines('\n'.join(sorted_dict))
    return output_file


if __name__ == '__main__':
    main(sys.argv)
