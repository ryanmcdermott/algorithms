def kadane(arr):
    curr = arr[0]
    global_max = arr[0]
    for i in range(1, len(arr)):
        curr = max(arr[i], arr[i] + curr)
        global_max = max(global_max, curr)

    return global_max
