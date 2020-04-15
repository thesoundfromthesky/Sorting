
import random

arr = []
arr.extend(range(0, 11))
random.shuffle(arr)


def quick_sort(arr, pivot=0):
    if len(arr) == 0:
        return []

    pivot = arr[pivot]

    lhs = []
    rhs = []
    mid = []
    for e in arr:
        if e < pivot:
            lhs.append(e)
        elif e > pivot:
            rhs.append(e)
        else:
            mid.append(e)

    return quick_sort(lhs) + mid + quick_sort(rhs)


# print(quick_sort(arr))

def quick_sort_in_place(arr, l, r):

    if r-l < 1:
        return arr

    pivot = l
    i = l+1
    j = r
    found_lhs = False
    found_rhs = False
    while i < j:
        while not found_lhs and i < j:
            if arr[j] < arr[pivot]:
                found_lhs = True
            else:
                j -= 1

        while not found_rhs and i < j:
            if arr[i] >= arr[pivot]:
                found_rhs = True
            else:
                i += 1

        if found_lhs and found_rhs:
            arr[i], arr[j] = arr[j], arr[i]
            found_lhs = False
            found_rhs = False
  
    if arr[pivot] > arr[i]:
        arr[pivot], arr[i] = arr[i], arr[pivot]

    quick_sort_in_place(arr, l, i-1)
    quick_sort_in_place(arr, i, r)

    return arr

sample2=[3,3,4,1,2]
# print(quick_sort_in_place(arr, 0, len(arr)-1))
print(quick_sort_in_place(sample2, 0, len(sample2)-1))

arr1 = []
arr1.extend(range(0, 8))

arr2 = []
arr2.extend(range(5, 9))

# TO-DO: complete the helpe function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    cur = 0
    i = 0
    j = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            merged_arr[cur] = arrA[i]
            cur += 1
            i += 1
        else:
            merged_arr[cur] = arrB[j]
            cur += 1
            j += 1

    while (i < len(arrA)):
        merged_arr[cur] = arrA[i]
        cur += 1
        i += 1

    while (j < len(arrB)):
        merged_arr[cur] = arrB[j]
        cur += 1
        j += 1

    return merged_arr

# print(merge(arr1,arr2))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    mid = len(arr) // 2

    if mid == 0:
        return arr

    lhs = arr[:mid]
    rhs = arr[mid:]

    arr = merge(merge_sort(lhs), merge_sort(rhs))

    return arr

# print(arr)
# print(merge_sort(arr))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    for i in range(mid, end+1):
        target = arr[i]
        for j in range(i - 1, start - 1, -1):
            if arr[j] > target:
                arr[j+1], arr[j] = arr[j], target
            else:
                break

    return arr

# sample = [*arr1, *arr2]
# print(sample)
# print(merge_in_place(sample, 0, len(arr1), len(sample)-1))


def merge_sort_in_place(arr, l, r):
    # TO-DO

    length = 1+r-l
    if length <= 1:
        return arr

    mid = (1+r+l) // 2

    merge_sort_in_place(arr, l, mid-1)
    merge_sort_in_place(arr, mid, r)

    merge_in_place(arr, l, mid, r)

    return arr

# print(arr)
# print(merge_sort_in_place(arr,0,len(arr)-1))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
