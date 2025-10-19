b = 20
a = 12
temp = 0

while b > 0:
    temp = b
    b = a % b
    a = temp

print(a)