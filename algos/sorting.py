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

def quicksort(arr):
    """
    This is quicksort. 

    O(n log n), it takes log n operations to sort but it has to go through 
    every element with comparing to the pivot. 

    previous knowledge: recursion, divide and conquer. :
    """
    if len(arr) < 2: 
        return arr
    else: 
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater) 


if __name__ == "__main__":
    arr = [2, 4, 6, 1, 7, 3, 5]
    # print(get_smallest(arr))
    # print(selection_sort(arr))
    
    print(quicksort(arr))
    
