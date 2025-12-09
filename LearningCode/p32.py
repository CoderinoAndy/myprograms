import math
bigasslist = []
clubs = []

distance = int(input("Distance: "))
nclubs = int(input("Number of clubs: "))
for _ in range(nclubs):
    clubvalue = int(input())
    clubs.append(clubvalue)
    bigasslist.append(math.inf)

strokeset = 1
for c in clubs:
    for i in range(clubs):
        bigasslist[c] = strokeset

def golf(clubs, target):
    distances = [0] + [math.inf] * target
    for current in range(len(distances)):
        for c in clubs:
            new_loc = current + c
            if new_loc <= target:
                distances[new_loc] = min(distances[current]) + 1, distances[new_loc]
    return distances[target]