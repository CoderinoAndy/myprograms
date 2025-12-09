# Recursive function that evaluates the power to its integer representation

def meow(number, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return number
    else:
        return number*meow(number, exponent - 1)

print(meow(6, 7))

def missing(array):
    limit = len(array)
    freq_table = {}
    for x in array:
        freq_table[x] = 1
    for i in range(0, limit+1):
        if i not in freq_table:
            return i
    return -1
# Faster than
# for x in range(0, limit + 1):
#   if x not in array:
#       return x
# return -1

