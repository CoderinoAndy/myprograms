def sumOfOddSquaresUnderNumber(n):
    total = 0
    number = 0
    while number <= 736000:
        squared = number**2
        if squared%2 != 0:
            total += squared
        number += 1
    return total

user_number = int(input("What's the number? "))