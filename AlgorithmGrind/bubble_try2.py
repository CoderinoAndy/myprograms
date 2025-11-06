# 99.99%
def bubble_try1(listy):
    if len(listy) <= 1:
        return listy
    else:
        length = len(listy)
        switched = True
        while switched:
            switched = False
            for x in range(1, length):
                if listy[x - 1] > listy[x]:
                    switched = True
                    listy[x - 1], listy[x] = listy[x], listy[x - 1]
        return listy
print(bubble_try1([1, 4, 1, 2, 6, 9]))