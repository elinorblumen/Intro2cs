
def is_it_summer_yet(thres, temp1, temp2, temp3):

    """This function checks whether at least two out of three recent temperature values have exceeded a certain
    threshold. The function receives four values: the threshold temperature and three temperature measurements,
    and returns one boolean value, True if at least two temperatures have exceeded the threshold, False if not"""

    warm_count = 0

    if temp1 > thres:
        warm_count = warm_count + 1

    if temp2 > thres:
        warm_count = warm_count + 1

    if temp3 > thres:
        warm_count = warm_count + 1

    if warm_count >= 2:
        return True

    else:
        return False
