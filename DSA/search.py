def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1
    
def BFS(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def DFS(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited




arr = [1,2,3,4,5]
print(arr[7 % len(arr)])  

binarySearch([1,2,3,4,5], 0, len(arr), 3)