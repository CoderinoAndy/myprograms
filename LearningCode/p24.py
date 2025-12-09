# add two values in a sorted list to get a target value, indexes must not repeat
def addylisty(a_list, target):
    # Brute force method --> F150
    if len(a_list) <= 1:
        return a_list
    else:
        for x in range(len(a_list) - 1):
            for y in range(x + 1, len(a_list)):
                if a_list[x] + a_list[y] == target:
                    return a_list[x], a_list[y]
        return -1
    
def meth3(alist, target):
    for i in range(len(alist) - 1):
        diff = target - a_list[i]
        for j in range(i + 1, len(alist))
            if alist[j] == diff:
                return True

def meth4(alist, target):
    pass

def meth5(alist, target):
    # assume alist already sorted
    right = len(alist) - 1
    left = 0
    while alist[left] < alist[right]:
        total = alist[left] + alist[right]
        if total == target:
            return True
        else:
            if total < target:
                left += 1
            if total > target:
                right -= 1
    return False
