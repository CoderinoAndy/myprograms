def select(a_list):
    if len(a_list) <= 1:
        return a_list
    else:
        i = 0
        while i < len(a_list):
            smallest = a_list[i] # then prove it is or it is not
            # hunt
            j = i + 1 # search from i + 1
            new_low_location = i # Initialize to i
            while j < len(a_list):
                new_value = a_list[j]
                if new_value < smallest:
                    smallest = new_value
                    new_low_location = j
                j += 1
            # endhunt
            # Swap smallest into proper location
            a_list[i], a_list[new_low_location] = a_list[new_low_location], a_list[i]
            i += 1

def bubble_sorter(arr):
    if len(arr) <= 1:
        return arr
    else:
        n = len(arr)
        while True:
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

def bubble(a_list):
    if len(a_list) <= 1:
        return a_list
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(a_list)):
            if a_list[i] < a_list[i - 1]:
                a_list[i - 1], a_list[i] = a_list[i], a_list[i - 1]
                swapped = True
        # end inner for
    # end outer while
    return a_list

def inserty(a_list):
    i = 1
    while i < len(a_list):
        j = i
        while j > 0:
            if a_list[j - 1] > a_list[j]:
                a_list[j - 1], a_list[j] = a_list[j], a_list[j-1]
            else:
                break
            j -= 1
        i += 1
    return a_list

def sortit(a_list, b_list):
    i = 1
    while i < len(a_list):
        j = i
        while j > 0:
            if a_list[j-1] > a_list[j]:
                a_list[j-1], a_list[j] = a_list[j], a_list[j-1]
                b_list[j-1], b_list[j] = b_list[j], b_list[j-1]
            else:
                break
            j -= 1
        i += 1
    return a_list, b_list

print(sortit([1, 2, 5, 6, 1], ["men", "den", "wen", "gen", "fen"]))