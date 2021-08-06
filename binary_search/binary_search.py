def binary_search(haystack, needle):
    if len(haystack) == 0:
        return -1

    l, r = 0, len(haystack) - 1

    while l <= r:
        mid = (l + r) // 2

        if needle < haystack[mid]:
            r = mid - 1
        elif needle > haystack[mid]:
            l = mid + 1
        else:
            return mid

    return -1
