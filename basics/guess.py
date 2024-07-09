from random import randint
def guess(n:int)-> int:
    pick = randint(1, 10)
    if n < pick:
        return 0 
    elif n > pick:
        return -1
    else:
        return 0

def guessNumber(n:int) -> int:
    low = 1
    high = 10
    while low <= high:
        mid = (low + high) // 2
        if guess(mid) == 0:
            return mid
        elif guess(mid) == -1:
            high = mid - 1
        else:
            low = mid + 1
    return -1