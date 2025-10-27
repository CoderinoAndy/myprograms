#Factor counter
number = int(input())
factor = 1
factor_count = 1
maximum = number//2
while factor <= maximum:
    if number % factor == 0:
        print(factor)
        factor_count += 1
    factor += 1
print(number)
print(f"{number} has {factor_count} factors.")
if factor_count == 2:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is a composite number.")
