def two_list(a_list, b_list):
    for term in a_list:
        b_list.append(term)
    b_list.sort()
    return b_list

print(two_list([1, 3, 5], [2, 7, 10]))
 
