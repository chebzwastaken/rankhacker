
def utopianTree(n):
    count = 0
    for i in range(n+1):
        if i % 2 != 0:
            count *= 2
        else: 
            count += 1
    return count


utopianTree(5)