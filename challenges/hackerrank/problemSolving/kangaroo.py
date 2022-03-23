def kangarooY(x1, v1, x2, v2):
    match = True
    count = 0
    while match:
        if x1 == x2:
            match = False
            return "YES"
        elif count > 1000:
            return "NO"
        else:
            x1 += v1
            x2 += v2 
            count += 1
    

print(kangaroo(0, 3, 8, 4))

def kangaroo(x1, v1, x2, v2):
    if v1 < v2:
        return "NO"
    elif x1 < x2:
        return "NO"
    elif v1 == v2:
        return "YES"
    else:
        return kangaroo(x1+1, v1+1, x2+1, v2+1)