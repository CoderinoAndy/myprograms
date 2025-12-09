chorelist = []

minutes_available = int(input())
chorechoose = int(input())
for _ in range(chorechoose):
    chorelist.append(int(input()))

if min(chorelist) > minutes_available:
    print("U CAN NOT DO")
else:
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(chorelist) - 1):
            if chorelist[i - 1] > chorelist[i]:
                chorelist[i - 1], chorelist[i] = chorelist[i], chorelist[i - 1]
                swapped = True
    
    counter = 0
    while minutes_available > 0 and chorelist:
        time_left -= chorelist[0]
        counter += 1
        chorelist.pop(0)
    print(counter)



