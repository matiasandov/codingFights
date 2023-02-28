def find_max(arr):
    max = 0
    for i in range (0, len(arr)):
        max = find(arr[i], max)
    return max
    
def find(act, max):
    if (act > max):
        max = act
    return max