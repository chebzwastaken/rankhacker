# rotate 2d array x degrees
def rotate(arr: list, degree: int):
    # rotate 90 degrees
    degree = degree % 360
    if degree == 0:
        return arr
    if degree == 90:
        return list(zip(*arr[::-1]))
    if degree == 180:
        return arr[::-1]
    if degree == 270:
        return list(zip(*arr)[::-1])
    return arr

print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 270))


