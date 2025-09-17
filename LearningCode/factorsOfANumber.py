number = int(input())
factor = 1
while factor <= number:
    if number % factor == 0:
        print(factor)
    factor += 1
