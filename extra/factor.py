
def factor(n):
    for d in range(1, n + 1):
       if n % d == 0:
           print(d)
factor(35)

def factor_op(n):
    for d in range(1, round(n**.5) + 1 ):
        if n % d == 0:
            print(d)

factor_op(35)

def factor_list(n):
    v = []
    for d in range(1, n + 1):
        if n % d == 0:
            v.append(d)
    print(v)