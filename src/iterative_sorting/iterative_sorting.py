import random

# seq=[]
# seq.extend(range(0, 5))
# random.shuffle(seq)
# print(f"{seq}\n")

# Your Task
# - Implement the `insertion_sort()` function in the Guided Project with your TA


def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        target = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > target:
                arr[j+1], arr[j] = arr[j], target
            else:
                break

# insertion_sort(seq)
# print(seq)


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        if(cur_index != smallest_index):
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr

# selection_sort(seq)
# print(seq)

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    is_swapped = True

    while is_swapped:
        is_swapped = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_swapped = True
    return arr

# bubble_sort(seq)
# print(seq)


# STRETCH: implement the Count Sort function below
count_arr = [2, 4, 5, 5, 1]


def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return arr

    minimum = min(arr)

    if(minimum < 0):
        return "Error, negative numbers not allowed in Count Sort"
        
    maximum = max(arr)
    count = {}
    for i in range(minimum, maximum+1):
        count[i] = 0
    
    for i in arr:            
        count[i] += 1
   
    keys = list(count.keys())
    keys.sort()
    for i in range(0, len(keys) - 1):
        cur = keys[i]
        nxt = keys[i + 1]
        count[nxt] += count[cur]

    sorting = [*arr]
   
    for i in sorting:
        arr[count[i]-1]=i
        count[i] -= 1
    return arr


print(count_sort(count_arr))
