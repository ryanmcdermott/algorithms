def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i = i + 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def do_quicksort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        do_quicksort(arr, left, pivot - 1)
        do_quicksort(arr, pivot + 1, right)

    return arr


def quicksort(arr):
    return do_quicksort(arr, 0, len(arr) - 1)
