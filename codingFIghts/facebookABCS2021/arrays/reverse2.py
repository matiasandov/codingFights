def reverseArray(a):
    result = []
    for i in a:
        result[i] = a[len(a) - 1 - i]
    return result