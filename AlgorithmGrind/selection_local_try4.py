def selection_local_try4(MyList):
    if len(MyList) <= 1:
        return MyList
    else:
        i = 0
        while i < len(MyList):
            j = i + 1
            new_lowcation = i
            smallest = MyList[i]
            while j < len(MyList):
                new_value = j
                if new_value < smallest:
                    smallest = new_value
                    new_lowcation = j
                j += 1
            MyList[i], MyList[new_lowcation] = MyList[new_lowcation], MyList[i]
            i += 1
        return MyList