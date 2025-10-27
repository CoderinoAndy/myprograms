def sieve_of_eratosthenes(n):
    if n == 2:
        return True
    elif n <= 1:
        return False
    elif n % 2 == 0:
        return False
    else:
        divider = 3
        while divider < (n**0.5 + 1):
            if n % divider == 0:
                return False
            divider += 2
        return True

while number <= 1000000:
    if sieve_of_eratosthenes(number):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
    