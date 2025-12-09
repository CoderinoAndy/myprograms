#Given a list move all 0s to the end of the list




def moveZeroes1(nums):
    zeroes = []
    non_zeroes = []
    for v in nums:
        if v == 0:
            zeroes.append(v)
        else:
            non_zeroes.append(v)
    nums = non_zeroes + zeroes
    return nums

def moveZeroes2(nums):
    temp = [0] * len(nums)
    i = 0
    for num in nums:
        if num != 0:
            temp[i] = num
            i += 1

def moveZeroesPro(mylist):
    swapped = True
    while swapped:
        swapped = False
        for element in range(len(mylist) - 1):
            if mylist[element] == 0 and mylist[element + 1] != 0:
                mylist[element], mylist[element + 1] = mylist[element + 1], mylist[element]
                swapped = True
    return mylist

    