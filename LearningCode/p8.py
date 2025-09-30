#Create a function that determines if the number is a "perfect" number.
#A perfect number is a number where the sum of its proper devisors equals the number itself.
import math

def is_perfect_number(n):
    start = 1
    holder = 0
    while start < int(math.sqrt(n)):
        if n % start == 0:
            holder += n
        start += 1
    return holder == n

def main():
    number = int(input("What is your number: "))
    if is_perfect_number(number):
        print(f"{number} is a perfect number")
    else:
        print(f"{number} is not a perfect number but we love it anyways")

main()