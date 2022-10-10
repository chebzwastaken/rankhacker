def plusMinus(arr):
    z_count = 0
    p_count = 0
    n_count = 0

    for i in arr: 
        if i > 0: 
            p_count += 1
        elif i < 0: 
            n_count += 1
        else: 
            z_count += 1
    
    print(n_count / len(arr))
    print(p_count / len(arr))
    print(z_count / len(arr))
    