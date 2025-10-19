n = 1216
x = 0

while n > 0:
    x = x + (n%10)
    n //= 10

print(x)