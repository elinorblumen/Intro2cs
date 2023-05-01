def quadratic_equation(a, b, c):

    """"This function is meant to receive three parameters: a, b, c
    and solve a quadratic of the form a*x**2 + b*x + c = 0"""

    discriminant = b**2 - (4*a*c)

    if discriminant < 0:
        return None, None

    elif discriminant > 0:
        solution_1 = (-b+discriminant**0.5)/2*a
        solution_2 = (-b-discriminant**0.5)/2*a
        return solution_1, solution_2

    else:
        solution_1 = -b/2*a
        return solution_1, None


def quadratic_equation_user_input():

    """This function is meant to receives input from user
    to solve a quadratic equation of the form a*x**2 + b*x + c = 0. the function will then
    print specific messages containing the solutions on to the screen. """

    input_values = input('Insert coefficients a, b and c: ').split(' ')

    a = float(input_values[0])
    b = float(input_values[1])
    c = float(input_values[2])

    results = quadratic_equation(a, b, c)

    if results[0] is None and results[1] is None:
        print('The equation has no solutions')

    elif results[1] is None:
        print('The equation has 1 solution: ' + str(results[0]))

    else:
        print('The equation has 2 solutions: ' + str(results[0]) + ' and ' + str(results[1]))
