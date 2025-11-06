# 75%
def selection_local_try2(MyList):
    if len(MyList) <= 1:
        return MyList
    else:
        i = 0
        while i < len(MyList):
            smallest = MyList[i]
            j = i + 1
            low_location = i
            while j < len(MyList):
                new_value = MyList[j]
                if new_value < smallest:
                    smallest = new_value
                    low_location = j
                j += 1
            MyList[i], MyList[low_location] == MyList[low_location], MyList[i]
            i += 1