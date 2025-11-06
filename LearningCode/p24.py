# add two values in a sorted list to get a target value, indexes must not repeat
def addylisty(a_list, target):
    if len(a_list) <= 1:
        return a_list
    else:
        for x in range(len(a_list) - 1):
            for y in range(x + 1, len(a_list)):
                if a_list[x] + a_list[y] == target:
                    return a_list[x], a_list[y]
        return -1

print(addylisty([1, 1, 2, 3, 4, 5, 6, 9], 6))