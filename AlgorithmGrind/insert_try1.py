# 60%
def insert_try1(listy):
    if len(listy) <= 1:
        return listy
    else:
        i = 1
        while i < len(listy):
            j = i
            while j > 0:
                if listy[j - 1] > listy[j]:
                    listy[j - 1], listy[j] = listy[j], listy[j - 1]
                else:
                    break
                j -= 1
            i += 1
        return listy
print(insert_try1([1, 2, 1, 2, 5, 6, 1, 7, 10, -100]))