def binarySearch(arr, target):
    low = 0 
    high = len(arr) - 1 

    while low <= high: 
        mid = (low + high) // 2 
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 
        else:
            return f"It's Here {arr[mid]}"
    return False 
    
print(binarySearch([1, 2, 3, 4, 5], 6))
