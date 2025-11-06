def least_great_search(a_list, target):
    if len(a_list) <= 1:
        return a_list
    elif target not in a_list:
        return -1
    else:
        current_value = 0
        search_index = len(a_list)//2
        while True:
            current_value = a_list[search_index]
            if current_value == target:
                return search_index
            if current_value > target:
                search_index = search_index + search_index//2
            else:
                search_index = search_index//2

def bin_search(a_list, target):
    low = 0
    high = len(a_list)
    while low < high:
        mid = (low + high)//2
        if a_list[mid] == target:
            return mid
        elif a_list[mid] > target:
            high = mid
        else:
            low = mid + 1
    return -1


print(least_great_search([1, 2, 3, 6, 8, 5000], 7))