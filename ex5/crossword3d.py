######################################################################################################
# FILE : crossword3d.py
# WRITERS : ElinorB, ReutB
# EXERCISE : Intro2cs ex5 2018
# DESCRIPTION : Crossword through 3d matrices
######################################################################################################

import os
import sys

NUM_PARAM = 5
WORDS_PARAM_NUM = 1
MATX_PARAM_NUM = 2
OUTPUT_PARAM_NUM = 3
DIRECTIONS_PARAM = 4
VALID_DIRECTION = "abc"
ALL_DIR = "udrlwxyz"

ERROR_PARAMETERS = "ERROR: invalid number of parameters. Please enter word_file matrix_file output_file directions"
ERROR_WORDS_FILE_NOT_EXIST = ["ERROR: Word file ", " does not exist"]
ERROR_FOR_MATX_NOT_EXIST = ["ERROR: Matrix file ", " does not exist"]
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

        all_word_list = original_word_list.readlines()
        original_word_list.close()
        word_list = [word.replace('\n', '') for word in all_word_list]
        all_word_list_low = [letter.lower() for letter in word_list]

        all_matrix = original_matx.readlines()
        original_matx.close()
        all_matrix_low = [letter.lower() for letter in all_matrix]

        matrix3d = divide_to_matrices(all_matrix_low)
        list_of_matrices = slice_matrix3d(matrix3d, directions)

        output_dict = dict()
        for matrix in list_of_matrices:
            run_crossword(all_word_list_low, matrix, output_dict, output_file, ALL_DIR)

        write_output(output_dict, output_file)
        output_file.close()


def divide_to_matrices(all_matrix_low):
    """
    A function meant to receive a list of matrices organized as lists of letters
    and return a list of lists of letters organized w/o commas
    :param The one and only original 3dmatrix
    :return: The 3dmatrix organized as 2dmatrices w/o commas
    """

    matrix3d = []
    matrix2d = []

    for line in all_matrix_low:
        temp_line = ""

        for letter in line:
            if letter == '\n':
                matrix2d.append(temp_line)
                break

            elif letter == '*':
                matrix3d.append(matrix2d)
                matrix2d = []
                break

            elif letter != ',':
                temp_line += letter

    matrix2d.append(temp_line)
    matrix3d.append(matrix2d)

    return matrix3d



def slice_matrix3d(matrix3d, directions):
    """
    A function meant to receive a 3dmatrix organized as lists of lists without commas and directions for the search
    and return a list of lists containing the 2dmatrices organized according to the specific directions.

    :param matrix3d: A 3dmatrix organized as 2dmatrices without commas
    :param directions: Direction "abc"
    :return: list of lists containing the 2dmatrices organized according to the specific directions
    """

    list_of_matrices = []

    if VALID_DIRECTION[0] in directions:
        for matrix2d in matrix3d:
            list_of_matrices.append(matrix2d)

    if VALID_DIRECTION[1] in directions:
        for i in range(len(matrix3d[0])):
            temp_matrix = []
            for matrix2d in matrix3d:
                temp_matrix.append(matrix2d[i])
            list_of_matrices.append(temp_matrix)

    if VALID_DIRECTION[2] in directions:
        matrix_columns = []
        for matrix2d in matrix3d:
            matrix_columns.append(lst_to_concat_line_lst(divide_to_columns(matrix2d)))

        for i in range(len(matrix_columns[0])):
            temp_matrix = []
            for matrix in matrix_columns:
                temp_matrix.append(matrix[i])
            list_of_matrices.append(temp_matrix)

    return list_of_matrices


def run_crossword(word_list, matrix, output_dict, output_file, directions):
    """
    Run the program to search words in given matrix and returns the words that were found w/ num of founds
    in matrix according to given directions
    :param original_word_list:list of all words to search in matrix in lower-cases letters
    :param matrix: lower-case letters matrix
    :param output_file: txt file
    :param directions: string of valid directions
    :return: new output.txt file with list of words found and times they were founded organized in alpha-bet order.
    """

    if word_list == [] or matrix == [[]]:
        write_output(output_dict, output_file)

    str_list_to_check = []  # list w/ all the strings of lines/columns/diagonals require by directions

    for single_direction in directions:
        if single_direction == 'u':
            str_list_to_check.append(mirror_all_lines_lst(divide_to_columns(matrix)))
            continue
        elif single_direction == 'd':
            str_list_to_check.append(divide_to_columns(matrix))
            continue
        elif single_direction == 'r':
            str_list_to_check.append(divide_to_lines(matrix))
            continue
        elif single_direction == 'l':
            str_list_to_check.append(mirror_all_lines_lst(divide_to_lines(matrix)))
            continue
        elif single_direction == 'w':
            str_list_to_check.append(mirror_all_lines_lst(divide_to_diagonal_d_to_l(matrix)))
            continue
        elif single_direction == 'x':
            str_list_to_check.append(mirror_all_lines_lst(divide_to_diagonal_d_to_r(matrix)))
            continue
        elif single_direction == 'y':
            str_list_to_check.append(divide_to_diagonal_d_to_r(matrix))
            continue
        elif single_direction == 'z':
            str_list_to_check.append(divide_to_diagonal_d_to_l(matrix))
            continue

    histogram(sum(str_list_to_check, []), word_list, output_dict)


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


def histogram(list_of_lines, word_list_low, output_dict):
    """
    A function meant to receive a list of lists representing the lines\
    diagonals in a given matrix and a list of words, a list of words
    to search for and a dictionary. The function checks if each
    word from the list is in the lists of lines and organises the information in a dictionary
    that contains only the word that appear in the lines and how many times each appeared.

    :param output_dict: Dictionary
    :param list_of_lines: list of strings lines to check
    :param word_list_low: A list of words

    """

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
                if word not in output_dict:
                    output_dict[word] = 1
                else:
                    output_dict[word] += 1


def write_output(output_dict, output_file):
    """
    Function will write and sort the words found in histogram()
    in an output file while sorting the words in an alphabetic order.
    :param output_dict: A dictionary containing all the words that appeared in the matrices and how many times
    :param output_file: A file to which all the output data is written onto
    """

    sorted_dict = []
    for key in sorted(output_dict):
        new_val = ''.join([str(key), ',', str(output_dict[key])])
        sorted_dict.append(new_val)

    output_file.writelines('\n'.join(sorted_dict))


if __name__ == '__main__':
    main(sys.argv)

