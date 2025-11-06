def bubble_ultimate(listy):
    if len(listy) <= 1:
        return listy
    else:
        switched = True
        length = len(listy)
        while switched:
            switched = False
            for x in range(1, length):
                if listy[x - 1] > listy[x]:
                    switched = True
                    listy[x - 1], listy[x] = listy[x], listy[x - 1]
        return listy

def selection_ultimate(listy):
    if len(listy) <= 1:
        return listy
    else:
        i = 0
        while i < len(listy):
            smallest = listy[i]
            new_lowcation = i
            j = i + 1
            while j < len(listy):
                new_value = listy[j]
                if new_value  < smallest:
                    smallest = new_value
                    new_lowcation = j
                j += 1
            listy[i], listy[new_lowcation] = listy[new_lowcation], listy[i]
            i += 1
        return listy

def insert_ultimate(listy):
    if len(listy) <= 1:
        return listy
    else:
        i = 1
        while i < len(listy):
            j = i
            while j > 0:
                if listy[j - 1] > listy [j]:
                    listy[j - 1], listy[j] = listy[j], listy[j - 1]
                j -= 1
            i += 1
        return listy

print(selection_ultimate([1, 2, 1, 3, -10]))
print(bubble_ultimate([1, 2, 1, 3, -10]))
print(insert_ultimate([1, 2, 1, 3, -10]))
        