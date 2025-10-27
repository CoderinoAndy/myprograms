def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        divider = 3
        upper_limit = num**0.5 + 1
        while divider < max(upper_limit, 3):
            if num % divider == 0:
                return False
            divider += 2
        return True

def main():
    num = 1
    while num <= 1000000:
        if is_prime(num):
            print(f"{num} is prime")
        else:
            print(f"{num} is not prime")
        num += 1


main()