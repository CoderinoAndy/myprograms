# Program that finds the given number of fibonaccis

def fib(n):
    if n in [0, 1]:
        return n
    else:
        location = 2 # because we already accounted for location 0 and 1
        one_back = 1
        two_back = 0
        while location <= n:
            current = one_back + two_back
            two_back = one_back
            one_back = current
            location += 1
        return current

print(fib(10))

