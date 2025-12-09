# Had to rely on example, 25%
def selection_local(listy):
    if len(listy) <= 1:
        return listy
    else:
        i = 0
        while i < len(listy):
            smallest = listy[i]
            j = i + 1
            low_location = i
            while j < len(listy):
                new_value = listy[j]
                if new_value < smallest:
                    smallest = new_value
                    low_location = j
                j += 1
            listy[i], listy[low_location] == listy[low_location], listy[i]
            i += 1
        