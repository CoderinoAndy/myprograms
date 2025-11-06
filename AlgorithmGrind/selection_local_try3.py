# 99%
def selection_local_try3(MyList):
    if len(MyList) <= 1:
        return MyList
    else:
        i = 0
        while i < len(MyList):
            smallest = MyList[i]
            j = i + 1
            new_lowcation = i
            while j < len(MyList):
                new_value = MyList[j]
                if new_value < smallest:
                    smallest = new_value
                    new_lowcation = j
                j += 1
            MyList[i], MyList[new_lowcation] == MyList[new_lowcation], MyList[i]
            i += 1