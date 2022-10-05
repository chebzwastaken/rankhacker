def validSolution(arr):
    n = 0
    g = 2
    t_count = 0
    count = 0
    s_arr = []
    full = True
    while full:
        for i in range(len(arr)):
            for j in range(n, n + 3):
                s_arr.append(arr[i][j])
            if i == g:
                g += 3
                for i in range(1, len(s_arr)):
                    if s_arr.count(i) == 1:
                        count += 1
                if count == 8:
                    t_count += 1
                    count = 0
                    s_arr = []
        n += 3
        g = 2
        if n >= 8:
            full = False
        
    if t_count == 9:
        return True
    else:
        return False

print(validSolution([
    [1, 3, 2, 5, 7, 9, 4, 6, 8],
    [4, 9, 8, 2, 6, 0, 3, 7, 5],
    [7, 0, 6, 3, 8, 0, 2, 1, 9],
    [6, 4, 3, 1, 5, 0, 7, 9, 2],
    [5, 2, 1, 7, 9, 0, 8, 4, 6],
    [9, 8, 0, 4, 2, 6, 5, 3, 1],
    [2, 1, 4, 9, 3, 5, 6, 8, 7],
    [3, 6, 0, 8, 1, 7, 9, 2, 4],
    [8, 7, 0, 6, 4, 2, 1, 3, 5]]))

