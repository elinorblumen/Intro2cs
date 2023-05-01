import math


def area_circle(radius):

    """ Function calculates area of a circle with a given radius (float/int) """

    return math.pi*(radius**2)


def area_rect(dim1, dim2):

    """ Function calculates area of a rectangle with given dimensions (float/int) """

    return dim1 * dim2


def area_trapeze(dim1, dim2, dim3):

    """ Function calculates area of a trapezoid given top and bottom edge dimensions (dim1, dim2)
    and height (dim3) (float/int) """

    return ((dim1 + dim2)/2) * dim3


def shape_area():

    """ Function calculates the area of a requested shape (circle, rectangle or trapezoid) from a user input
    of shape and the required dimensions. Function returns the calculated area (float)"""

    choose_shape = int(input("Choose shape (1=circle, 2=rectangle, 3=trapezoid): "))

    if choose_shape == 1:
        radius = float(input(''))
        return area_circle(radius)

    elif choose_shape == 2:
        dimension1 = float(input(''))
        dimension2 = float(input(''))
        return area_rect(dimension1, dimension2)

    elif choose_shape == 3:
        dimension1 = float(input(''))
        dimension2 = float(input(''))
        dimension3 = float(input(''))
        return ((dimension1 + dimension2)/2) * dimension3

    else:
        return None
