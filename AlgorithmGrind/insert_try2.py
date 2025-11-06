def insert_try2(listy):
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
print(insert_try2([1, 2, 1, 6, -10]))