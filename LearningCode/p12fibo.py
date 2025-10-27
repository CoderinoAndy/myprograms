def fibonacci_num(n):
    if n in {0, 1}:
        return n
    else:
        location = 2
        second_back = 0
        first_back = 1
        total_sum = 0
        while location <= n:
            total_sum = second_back + first_back
            second_back = first_back
            first_back = total_sum
            location += 1
        return total_sum

# 0, 1, 1
# total sum = 1
# Second_back = 1
# first_back = 1
# location = 3
# Return total sum = 1

n = 1
while n < 10:
    print(fibonacci_num(n))
    n += 1