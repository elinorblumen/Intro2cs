####################################################################################
# FILE NAME: ex6
# WRITER: ElinorB
# EXERCISE: ex6
# DESCRIPTION: Recursion
####################################################################################

lst_to_n = []
a_lst = []




def print_to_n(n):
    """
    A function meant to receive an integer n and print all integers from 1 to n
    in increasing order.
    :param n: An integer
    """


    if n < 1:
        return None

    elif n == 1:
        n = 1

    elif n > 1:
        print_to_n(n-1)

    print(n)



def print_reversed(n):
    """
    A function meant to receive an integer n and print all integers from n to 1 in
    decreasing order.
    :param n: An integer
    """

    if n < 1:
        return None

    elif n == 1:
        print(1)

    elif n > 1:
        print(n)
        print_reversed(n-1)



def is_prime(n):
    """
    Function meant to receive an integer n and return True if n is a prime number
    and False otherwise.
    :param n: An integer
    :return: True if prime, False if not prime
    """


    if n < 2 or has_divisor_smaller_than(n, n) == 0:
        return False

    else:
        return True



def has_divisor_smaller_than(n, i):
    """
    Function meant to receive integers n and i and return False(!!!) if n has a divisor
    (other than 1) smaller than i and True if it doesn't.
    :param n: A positive integer other than 1
    :param i: A positive integer other than 1
    """


    if i == 2:
        return True

    elif i > 2:
        return (n % (i-1) != 0) and has_divisor_smaller_than(n, i-1)



def list_to_n(n):
    """
    Function meant to receive an integer n and return a list of positive integers
    in increasing order from 1 to the absolute value of n.
    :param n: An integer n
    :return: A list of positive integers from 1 to abs(n)
    """


    n = abs(n)

    if n == 0:
        return lst_to_n[::-1]

    else:
        lst_to_n.append(n)
        return list_to_n(n-1)



def divisors_list(n, i):
    """
    Function meant to receive two non-negative integers n and i and return a list of all
    numbers from 1 to i that divide n.
    :param n: Non-negative int
    :param i: Non-negative int
    """


    if i == 0:
        return []

    elif n % i == 0:
        return divisors_list(n, i-1) + [i]

    else:
        return divisors_list(n, i-1)



def divisors(n):
    """
    Function meant to receive an integer n and return a list of all numbers from 1 to
    n's absolute value that divide n.
    :param n: An integer
    :return: A list of positive integers
    """


    n = abs(n)

    return divisors_list(n, n)



def n_factorial(n):
    """
    Function meant to receive a non-negative integer n and return n! (n factorial)
    :param n: A non negative int
    :return: n factorial
    """


    if n == 0:
        return 1

    elif n > 0:
        return n_factorial(n-1)*n



def exp_n_x(n, x):
    """
    Function receives a non-negative int n and a reel number x
    and returns the exponential sum of x with relation to n.
    :param n: A non negative int
    :param x: A real number
    :return: exp(x) with relation to n
    """


    if n == 0:
        return 1

    elif n > 0:
        return exp_n_x(n-1, x) + x**n/n_factorial(n)



def play_hanoi(hanoi, n, src, dest, temp):
    """
    Function receives given number of discs, definition of source pole, destination pole,
    and temporary pole. and solves the 'Game of Hanoi' for the given parameters.
    :param n: Number of disks
    :param src: 'start' pole
    :param dest: 'destination' pole
    :param temp: 'temporary' pole
    """


    if n <= 0:
        return None

    elif n == 1:
        hanoi.move(src, dest)

    elif n == 2:
        hanoi.move(src, temp)
        play_hanoi(hanoi, n-1, src, dest, temp)
        hanoi.move(temp, dest)

    elif n == 3:
        play_hanoi(hanoi, n-1, src, temp, dest)
        hanoi.move(src, dest)
        play_hanoi(hanoi, n-1, temp, dest, src)

    else:
        play_hanoi(hanoi, n-1, src, temp, dest)
        hanoi.move(src, dest)
        play_hanoi(hanoi, n-1, temp, dest, src)



def print_binary_sequences_with_prefix(prefix, n):
    """
    Function receives a prefixed string and an integer n
    and prints all possible combination of the prefix with zeroes
    and ones added to it who's length is n.
    :param prefix: String
    :param n: Integer
    :return: Prints all possible sequences length n
    """


    if len(str(prefix)) == n:
        print(prefix)

    elif len(str(prefix)) < n:

        print_binary_sequences_with_prefix(str(prefix) + '0', n)
        print_binary_sequences_with_prefix(str(prefix) + '1', n)

    else:
        return None



def print_binary_sequences(n):
    """
    Function meant to receive a non negative integer n and print all
    possible sequences of 0's and 1's who's length equals n.
    :param n: A non negative integer
    """


    print_binary_sequences_with_prefix('', n)



def print_sequences_with_prefix(prefix, char_list, n):
    """
    Function receives a prefixed string, a list of characters
    and an integer n. and prints all possible combinations of
    the prefix with characters from the list, who's length is n.
    :param prefix: A strif
    :param char_list: A list of characters
    :param n: A non negative integer
    """


    if len(str(prefix)) == n:
        print(prefix)

    elif len(str(prefix)) < n:
        for x in char_list:
            print_sequences_with_prefix(str(prefix) + str(x), char_list, n)

    else:
        return None



def print_sequences(char_list, n):
    """
    Function receives a list of characters and a non negative integer
    and prints all possible combinations of characters from the list,
    who's length is equals n.
    Functions uses 'print_sequences_with_prefix' function.
    :param char_list: A list of characters
    :param n: A non-negative integer
    """


    prefix = ''

    print_sequences_with_prefix(prefix, char_list, n)



def print_no_repetition_sequences_with_prefix(prefix, char_list, n):
    """
    Function meant to receive a prefixed string, a list of different
    characters and an integer n, and print all possible sequences
    of the letters in the list, who's length equals n and non
    of the characters repeats itself in the sequence.
    :param prefix: String
    :param char_list: A list of different characters
    :param n: An integer n
    """


    if len(str(prefix)) == n:
        print(prefix)

    elif len(str(prefix)) < n:
        for x in char_list:
            new_char_list = char_list.copy()
            new_char_list.remove(x)
            print_no_repetition_sequences_with_prefix(str(prefix) + str(x), new_char_list, n)

    else:
        return None



def print_no_repetition_sequences(char_list, n):
    """
    Function receives a list of characters and an integer n and prints
    all possible sequences of letters from the the list who's length
    equals n and in which non of the characters repeats itself.
    :param char_list: A list of characters
    :param n: An integer n
    """


    prefix = ''

    print_no_repetition_sequences_with_prefix(prefix, char_list, n)



def no_repetition_sequences_list_with_prefix(prefix, output_lst, char_list, n):
    """
    A function meant to receive a prefixed string, a list of characters, a
    non-negative integer n and an output lst. The function updates the output list
    and adds to it all possible sequences of letters from the list who's length
    equals n and that non of the characters repeats itself in.
    :param prefix: A prefixed string
    :param output_lst: An outsourced list
    :param char_list: A list of characters
    :param n: A non-negative integer n
    """


    if len(str(prefix)) == n:
        output_lst += [str(prefix)]
        return


    elif len(str(prefix)) < n:
        for x in char_list:
            new_char_list = char_list.copy()
            new_char_list.remove(x)
            no_repetition_sequences_list_with_prefix(str(prefix) + str(x), output_lst, new_char_list, n)



def no_repetition_sequences_list(char_list, n):
    """
    Function meant to receive a list of characters and a non-negative integer n
    and return a list of all possible sequences of characters from the list who's
    length equals n and non of the characters repeats itself.
    :param char_list: A list of characters
    :param n: A non negative integer
    """


    prefix = ''
    output_lst = []

    no_repetition_sequences_list_with_prefix(prefix, output_lst, char_list, n)

    return output_lst





























