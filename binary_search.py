import time
import random

# scans the entire list in order to find the target  
def naive_search(sorted_list, target):
    for i in range(len(sorted_list)):
        if sorted_list[i] == target:
            return i
    return -1

# recursively divide the list until the target is found
def binary_search(sorted_list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None: 
        high = len(sorted_list) - 1
    if high < low:
        return -1

    midpoint = (low + high) // 2
    if sorted_list[midpoint] == target:
        return midpoint
    elif target < sorted_list[midpoint]:
        return binary_search(sorted_list, target, low, midpoint - 1)
    else:
        return binary_search(sorted_list, target, midpoint + 1, high)

# main function calls functions and records time to find target
if __name__=="__main__":
    length = 10000
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end-start)/length*1000000,"microseconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end-start)/length*1000000,"microseconds")