
def create_list():
    """Function is meant to receive inputs from user until it receives an empty input,
    and then return a list containing all inputs given up until the empty input. """

    string_from_user = input()
    list_list = []

    while string_from_user != '':
        list_list.append(string_from_user)
        string_from_user = input()

    return list_list


def concat_list(str_list):
    """parameter_1 type = list
    Function is meant to receive a list containing strings only
    and return a concatenation of the strings in the list."""

    str_str = ''

    for i in range(len(str_list)):

        str_str = str_str + str_list[i]

    return str_str


def average(num_list):
    """param_1 type = list
    Function is meant to receive a list of numbers and return the
    arithmetic average of the numbers in the list."""

    num_num = 0

    if len(num_list) == 0:
        return None

    else:

        for i in range(len(num_list)):
            num_num = num_num+num_list[i]

        return num_num/len(num_list)


def cyclic(lst1, lst2):
    """Function is meant to receive two lists,
    function will return 'True' if one list is a cyclic permutation of the other,
    otherwise, function will return 'False'"""

    if len(lst1) != len(lst2):
        return False

    elif lst1 == lst2 == []:
        return True

    for i in range(len(lst2)):
        if lst1[0] == lst2[i]:
            step = i
            if cyclic_check(lst1, lst2, step) != 0:
                return True
    else:
        return False


def cyclic_check(param_1, param_2, param_3):
    """param_1 type = list, pram_2 type = list, param_3 type = int
    Function is meant to find a cyclic permutation in two given lists
    and return value: True, if such exists. else function will return False.
    both lists must be same size!"""

    for l in range(len(param_2)):
        if param_1[l] != param_2[(param_3+l) % len(param_1)]:
            return False


def histogram(n, num_list):
    """param_1 ('n') type : int
    param_2 (num_list) type: list
    'num_list'- is a list consisting of integers within range('n')
    Function is meant to receive two parameters, and return a list whose elements are integers.
    the index number i of the elements in the output list represent the integer i within range(n),
    the int appearing in the output list in spot i represents the number of times the number i
    appeared in the second parameter (num_list)."""

    hist_list = []

    for i in range(n):
        counter = 0
        for m in range(len(num_list)):
            if i == num_list[m]:
                counter += 1
        hist_list.append(counter)

    return hist_list


def prime_factors(n):
    """parameter_1 type = int
    Function is meant to receive one natural number as input and return its prime
    factorization as output, while listing them by increasing order."""

    my_list = []

    if n == 1:
        return my_list
    else:
        for i in range(2, n+1):
            while n % i == 0:
                my_list.append(i)
                n = n/i
                if n == 1:
                    return my_list


def cartesian(lst1, lst2):
    """parameter_1 type = list, parameter_2 type = list
    Function is meant to receive two lists and return a list
    containing the cartesian product of the lists."""

    cartesian_list = []

    for l in range(len(lst1)):
        for i in range(len(lst2)):
            cartesian_list.append((lst1[l], lst2[i]))

    return cartesian_list


def pairs(n, num_list):
    """parameter_1 type = int, parameter_2 type = list
    Function is meant to receive one integer('n') and return number pairs from the list whose sum equals 'n'."""

    list_list = []
    for i in range(len(num_list)):
        for l in range(i+1, len(num_list)):
            if num_list[i]+num_list[l] == n:
                list_list.append([num_list[i], num_list[l]])
    return list_list
