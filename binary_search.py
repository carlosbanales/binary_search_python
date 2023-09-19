def naive_search(ordered_list, target):
    for i in range(len(ordered_list)):
        if ordered_list[i] == target:
            return i
    return -1
