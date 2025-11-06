a = 5
b = 2
c = 9

while b < c:
    a = a + b
    c = c - a
    if c < 0:
        b = b + 3
    else:
        b = b + a

print(a, b, c)