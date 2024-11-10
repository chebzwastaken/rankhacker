def get_smallest(arr):
    smallest = float('inf')
    smallest_index = 0  
    for i in range(len(arr)):
        if arr[i] < smallest: 
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    """
    This is Selection Sort. 

    O(n^2) technically O(n * 0.5 * n) as we go through 1 less element 
    each time, but whatever. 
    """
    new_arr = []
    for _ in range(len(arr)):
        new_arr.append(arr.pop(get_smallest(arr)))
    return new_arr

arr = [2, 4, 6, 1, 7, 3, 5]
print(get_smallest(arr))
print(selection_sort(arr))

