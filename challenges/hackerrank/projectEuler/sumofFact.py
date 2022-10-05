def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def f(n):
    n_arr = [int(i) for i in str(n)]
    sum = 0
    # factorial 
    for i in n_arr:
        sum += factorial(i)
    return sum

def sf(n):
    n_arr = [int(i) for i in str(n)]
    sum = 0
    for i in n_arr:
        sum += i
    return sum

def g(i):
    # check whether sf(f(n)) = i
    n = 1
    while 1:
        if sf(f(n)) == i:
            return n
        else:
            n += 1

def sg(i):
    # sum of g(i)
    n = [int(i) for i in str(g(i))]
    sum = 0
    for i in n:
        sum += i
    return sum

# how do i calculate summation? 

def summationSG(i):
    sum = 0
    n = 1
    while n <= i:
        sum += sg(n)
        n += 1
    return sum


print(f(342))