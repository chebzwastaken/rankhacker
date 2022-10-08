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

def MiniMaxSum(arr):
    arr.sort()
    print(sum(arr[:4]), sum(arr[1:]))
    
if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    print(rminiMaxSum(arr))
