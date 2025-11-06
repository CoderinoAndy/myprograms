def mean(data):
    if len(data) <= 1:
        return data
    else:
        total = 0
        for num in data:
            total += num
        return total/len(data)

def median(data):
    if len(data) <= 1:
        return data
    else:
        # begin sorting
        switch = True
        while switch:
            switch = False
            for i in range(1, len(data)):
                if data[i - 1] > data[i]:
                    switch = True
                    data[i - 1], data[i] = data[i], data[i - 1]
        # end sorting
        length = len(data)
        if len(data) % 2 == 0:
            mid = length//2
            left = mid - 1
            median = (data[mid] + data[left])/2
            return median
        else:
            return data[len(a_list)//2]

data = [2, 3, 3, 6, 5, 9, 10, 100, 14, 17]
result = median(data)
print(f"result (aka median) is {result}")