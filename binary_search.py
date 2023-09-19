

def naive_search(ordered_list, target):
    for i in range(len(ordered_list)):
        if ordered_list[i] == target:
            return i
    return -1

def binary_search(ordered_list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None: 
        high = len(ordered_list) - 1
    if high < low:
        return -1

    midpoint = (low + high) // 2
    if ordered_list[midpoint] == target:
        return midpoint
    elif target < ordered_list[midpoint]:
        return binary_search(ordered_list, target, low, midpoint - 1)
    else:
        return binary_search(ordered_list, target, midpoint + 1, high)
    
