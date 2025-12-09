clubs = []
target = int(input())
nclubs = int(input())
for _ in range(nclubs):
    club = int(input())
    clubs.append(club)
d = clubs
smallest = min(clubs)
counter = 1
impossible = False

while target not in d and not impossible:
    temp = []
    for c in clubs:
        for i in range(len(d)):
            temp.append(d[i] + c)
    counter += 1
    d = temp
    if counter >= target/smallest:
        print("Impossible")
        impossible = True
        break
if not impossible:
    print(counter)