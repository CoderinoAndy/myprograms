def EvenFibo(maximum):

    currentterm = 3
    total_sum = 2

    two_behind = 1
    one_behind = 2

    while currentterm <= maximum:
        two_behind = one_behind
        one_behind = currentterm
        currentterm = two_behind + one_behind

        if currentterm % 2 == 0:
            total_sum += currentterm

    return total_sum
        
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

print(EvenFibo(4000000))