def calculate_mathematical_expression(number_1, number_2, operation):

    """ This function is meant to recieve three paremteres from the user
    (two numbers and and one of the four elemantry arithmetic operations)
    and return the outcome of the calculation.
    number_1 and number_2 are of type 'float'
    operation is of type 'string' """

    if operation == '+':
        return number_1 + number_2

    elif operation == '-':
        return number_1 - number_2

    elif operation == '/' and number_2 != 0:
        return float(number_1) / float(number_2)

    elif operation == '*':
        return number_1 * number_2

    else:
        return None


def calculate_from_string(number_operation_number):

    """This function is meant to recieve a string parameter of the form:'number operation number'
     while 'operator' is meant to be one of the elementry arithmetic operations.
     The function will then return the calculation result."""

    input_str = number_operation_number.split(' ')
    return calculate_mathematical_expression(float(input_str[0]), float(input_str[2]), input_str[1])
