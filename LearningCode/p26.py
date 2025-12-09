def dictfactorizer(upper):
    thedict = {}
    for number in range(2, upper + 1):
        listfactor = []
        for possible_factor in range(1, number + 1):
            if number%possible_factor == 0:
                listfactor.append(possible_factor)
        thedict[number] = listfactor
    return thedict
upper = int(input())
print(dictfactorizer(upper))
