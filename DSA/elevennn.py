A = [10, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def elevennn(A):
    for i in A:
        if i < 10:
            return False
    return True
print(elevennn(A))