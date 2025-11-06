# A sorting algorithm that uses two lists: a sorted list and an unsorted list.
# Brings values into the sorted list in a sorted way/style
def select_multi(listy):
    if len(listy) <= 1:
        return listy
    else:
        sort = []
        while listy:
            smallest = listy[0]
            for element in listy:
                if element < smallest:
                    smallest = element
            sort.append(smallest)
            listy.remove(smallest)
        return sort

name = list(input("Name: "))
print(select_multi(name))
