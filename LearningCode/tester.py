def even_odd(listy):
    if not listy:
        return listy
    else:
        even = 0
        odd = 0
        even_list = []
        odd_list = []
        for number in listy:
            if number%2 == 0 or number == 0:
                even += 1
                even_list.append(number)
            else:
                odd += 1
                odd_list.append(number)
        if even > odd:
            return even_list
        elif even < odd:
            return odd_list
        else:
            return []

print(even_odd([8, 1]))