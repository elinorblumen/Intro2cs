def largest_and_smallest(number_1, number_2, number_3):

    """This function receives three numeric parameters and returns two values, first value
     is the largest number of the three and second value is the smallest number of the three."""

    if number_1 >= number_2:
        if number_1 >= number_3:
            largest = number_1
            if number_2 >= number_3:
                smallest = number_3
            else:
                smallest = number_2
        else:
            largest = number_3
            smallest = number_2

    elif number_2 >= number_3:
        largest = number_2
        if number_3 >= number_1:
            smallest = number_1
        else:
            smallest = number_3

    else:
        largest = number_3
        smallest = number_1

    return largest, smallest
