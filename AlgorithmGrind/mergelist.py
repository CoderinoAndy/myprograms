def mergelist(monliste):
    # Consider me as the splitter
    # Base case
    if len(monliste) <= 1:
        return monliste
    else:
        # Work toward the base case
        mid = len(monliste//2)
        first_half = monliste[:mid]
        second_half = a_list[mid:]

        first_half = mergelist(first_half) # recursive call
        second_half = mergelist(second_half) # another one
        return combine(first_half, second_half)

def combine(left, right):
    # Assume that right and left are sorted
    if len(left) == 0 and len(right) == 0:
        return []
    elif len(left) == 0:
        return right
    elif len(right) == 0:
        return left
    else:
        # here both left and right have values
        i = 0 # left
        j = 0 # right
        answer = [] #sorted things in here
        while i < len(left) and j < len(right):
            if left[i] < right[i]:
                answer.append(left[i])
                i += 1
            else:
                answer.append(right[i])
                j += 1
        # Values left over
        while i < len(left):
            answer.append(left[i])
            i += 1
        while j < len(right):
            answer.append(right[j])
            j += 1
        return answer


