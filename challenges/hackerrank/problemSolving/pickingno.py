def pickingNumbers(a):
    arr = [0] * (max(a) + 1)
    for i in range(len(a)):
        arr[a[i]] = a.count(a[i])
        print(arr)

    arr = [arr[i:i+2] for i in range(0, len(arr)) if arr[i] > 0]
    highest = max([sum(i) for i in arr])
    print(highest)
    
    # print(arr.index(max(arr)))
    # TODO: group elements together and count the number of elements in each group
    # like a merkle tree

    # return count

pickingNumbers([4, 2, 3, 4, 4, 9, 98, 98, 3, 3, 3, 4, 2, 98, 1, 98, 98, 1, 1, 4, 98, 2, 98, 3, 9, 9, 3, 1, 4, 1, 98, 9, 9, 2, 9, 4, 2, 2, 9, 98, 4, 98, 1, 3, 4, 9, 1, 98, 98, 4, 2, 3, 98, 98, 1, 99, 9, 98, 98, 3, 98, 98, 4, 98, 2, 98, 4, 2, 1, 1, 9, 2, 4])
# pickingNumbers([4, 6, 5, 3, 3, 1])
# pickingNumbers([1, 1, 2, 2, 4, 4, 5, 5, 5])



def bubblesort(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            print(a[j], a[j + 1])
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
# bubblesort([4, 6, 5, 3, 3, 1])
