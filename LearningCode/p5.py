import math

start = 1
num = int(input("Enter a value: "))
factor_count = 0
new_stop = int(math.sqrt(end)) + 1
while start < new_stop
    if num % start == 0:
        dividend = num//start
        if start != dividend:
            factor_count += 2
        else:
            factor_count += 1
        start += 1
print()