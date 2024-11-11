def _sum(arr):
    if len(arr) == 1: 
        return arr[0]
    if len(arr) <= 0:
        return 0
    
    
    return arr[0] + _sum(arr[1:])

print(_sum([1, 2, 3, 4]))