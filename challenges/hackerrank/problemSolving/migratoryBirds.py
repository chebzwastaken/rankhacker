import os

def migratoryBirds(arr):
    bird_count = [0] * len(arr)
    for i in range(len(arr)):
        bird_count[arr[i]] += 1
    max_count = max(bird_count)
    return bird_count.index(max_count)


mirgraph = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4, 5]
print(migratoryBirds(mirgraph))

print(mirgraph.index(max(mirgraph)))
# so if you want to get the index of the max value in a list, you can use the .index() method.
# bare in mind that it gets the max value that appears first in the list.
# so inverting the list and using the .index() method will get you the index of the max value that appears last in the list.