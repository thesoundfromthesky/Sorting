import random

seq=[]
seq.extend(range(0, 5))
random.shuffle(seq)
print(f"{seq}\n")

# Your Task
# - Implement the `insertion_sort()` function in the Guided Project with your TA
def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        target=arr[i]
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
            arr[cur_index], arr[smallest_index] =arr[smallest_index],arr[cur_index]

    return arr

# selection_sort(seq)
# print(seq)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    
    is_swapped = True

    while is_swapped:
         is_swapped=False
         for i in range(0, len(arr)-1):
             if arr[i] > arr[i+1]:
                 arr[i], arr[i+1] = arr[i+1], arr[i]
                 is_swapped=True
    return arr

# bubble_sort(seq)
# print(seq)

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
