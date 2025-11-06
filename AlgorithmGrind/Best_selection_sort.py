def select_sort(a_list):
    """
    Sorts a list in ascending order using the selection sort algorithm.

    Parameters:
        a_list (list): The list of elements to be sorted.

    Returns:
        list: A new list containing the sorted elements in ascending order.
    """
    new_list = []
    while len(a_list) > 0:
        smallest = min(a_list)
        new_list.append(smallest)
        a_list.remove(smallest)
    return new_list