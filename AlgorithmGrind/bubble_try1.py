# 80%
def bubble(MyList):
    if len(MyList) <= 0:
        return MyList
    else:
        length = len(MyList)
        switched = True
        while switched:
            switched = False
            for i in range(1, length):
                if MyList[i - 1] > MyList[i]:
                    switched = True
                    MyList[i], MyList[i - 1] = MyList[i - 1], MyList[i]
        return MyList

print(bubble([1, 2, 5, 1, 3, 1]))