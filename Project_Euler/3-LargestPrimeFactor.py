# Listing a given number's (in this case, according to the problem, 600851475143) prime factors (factors which are prime)
# This method is highly inefficient

number = 600851475143
primefactors = []
factor = 2

while factor <= int(number**0.5 + 1):
    is_composite = True
    if number % factor == 0:
        is_composite = False
        interfactor = 2
        while interfactor <= int((factor**0.5 + 1)) and interfactor != factor:
            if factor % interfactor == 0:
                is_composite = True
                break
            interfactor += 1

        if not is_composite:
            primefactors.append(factor)

    factor += 1

print(max(primefactors))