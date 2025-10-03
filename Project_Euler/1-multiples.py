# If we list all natural numbers below 10 that are multiples of 3, 5, 6, and 9. The sum of these multiples is 23. 
# Find the sum of all the multiples of 3 and 5 below 1000!

def finding_multiples(n):
    sum = 0
    for number in range(1, n):
        if number % 3 == 0:
            sum += number
        elif number % 5 == 0:
            sum += number
        elif number % 6 == 0:
            sum += number
        elif number % 9 == 0:
            sum += number
    return sum

print(finding_multiples(1000))