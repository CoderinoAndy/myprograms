#100%
def bubble_try3(listy):
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
print(bubble_try3([1, 0, 10, -10, 2]))