def uniqueNumber(arr):
    dicc = {}
    
    for i in range(len(arr)):
        if i not in dicc:
            dicc[i] = 1
        else:
            dicc[i] += 1
            
    for key, value in dicc.items():
        if value == 1:
            return dicc[key]

print(uniqueNumber([1,2,2,3,3]))
