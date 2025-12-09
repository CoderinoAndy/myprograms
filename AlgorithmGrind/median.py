def median(listy):
    if len(listy) == 0:
        return listy
    else:
        length = len(listy)
        if length % 2 == 0:
            right = length//2
            left = right - 1
            median = (listy[right] + listy[left])/2
            return median
        else:
            return listy[length//2]