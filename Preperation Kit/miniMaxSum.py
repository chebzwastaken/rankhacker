import sys 
def miniMaxSum(arr):
    # Write your code here
    i = 0
    count = 0
    suml = []
    while count != len(arr):
        ele = arr.pop(i)
        suml.append(sum(arr))
        arr.append(ele)
        count += 1
    
    return min(suml), max(suml)

def rminiMaxSum(arr):

    arr.sort()
    return sum(arr) - max(arr), sum(arr) - min(arr)

print(rminiMaxSum([1, 3, 5, 7, 9]))