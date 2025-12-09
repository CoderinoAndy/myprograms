def selecton_local_try5(listy):
    i = 0
    while i < len(listy):
        smallest = listy[i]
        j = i + 1
        new_lowcation = i
        while j < len(listy):
            new_value = listy[j]
            if new_value < smallest:
                smallest = new_value
                new_lowcation = new_value
            j += 1
        listy[i], listy[new_lowcation] = listy[new_lowcation], listy[i]
        i += 1
    return listy
def selection_local_try6(listy):
    i = 0
    while i < len(listy):
        j = i + 1
        new_lowcation = i
        smallest = listy[i]
        while j < len(listy):
            new_value = listy[j]
            if new_value < smallest:
                smallest = new_value
                new_lowcation = j
            j += 1
        listy[i], listy[new_lowcation] = listy[new_lowcation], listy[i]
        i += 1
    return listy
def selection_local_try7(listy):
    if len(listy) <= 1:
        return listy
    else:
        i = 0
        while i < len(listy):
            loc = i
            smol = listy[i]
            j = i + 1
            while j < len(listy):
                new_value = j
                if new_value < smol:
                    smol = new_value
                    loc = j
                j += 1
            listy[i], listy[loc] = listy[loc], listy[i]
            i += 1
        return listy
def selection_local_try8(listy):
    if len(listy) <= 1:
        return listy
    else:
        i = 0
        while i < len(listy):
            loc = i
            j = i + 1
            smol = listy[i]
            while j < len(listy):
                new_val = j
                if new_val < smol:
                    smol = new_val
                    loc = j
                j += 1
            listy[i], listy[loc] = listy[loc], listy[i]
            i += 1
        return listy
def selection_local_try9(listy):
    if len(listy) <= 1:
        return listy
    else:
        i = 0
        while i < len(listy):
            loc = i
            smol = listy[i]
            j = i + 1
            while j < len(listy):
                nval = j
                if nval < smol:
                    smol = nval
                    loc = j
                j += 1
            listy[i], listy[loc] = listy[loc], listy[i]
            i += 1
        return listy

        