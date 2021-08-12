import random


def fisher_yates(arr, seed=0):
    random.seed(seed)
    for i in range(len(arr) - 1, 0, -1):
        j = random.randrange(0, i)
        arr[i], arr[j] = arr[j], arr[i]

    return arr
