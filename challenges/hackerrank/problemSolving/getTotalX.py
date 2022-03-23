def getTotalY(a, b):

    # get factors of n:
    poss = []
    fact = []
    count = 0
    check = True
    while check:
        for x in range(1, 100 + 1):
            if set(a).issubset(set([i for i in range(1, x + 1) if x % i == 0])):
                # Getting integers that are have the factors contained in a
                poss.append(x)
        for i in poss:
            for j in b:
                if j % i == 0:
                    fact.append(i)
        for i in range(len(fact)):
            if fact.count(fact[i]) == len(b):
                count += 1

        if len(fact) > 0:
            check = False
        else:
            poss = []
    print(fact, int(count **.5))
    return len(fact)
        # if elements in b contain factors equal to the elements in fact then add to new array\
        

        


# print(getTotalY([2,6],[24, 36]))
# print(getTotalY([2,4],[16,32,96]))

# def factor(n):
#     for d in range(1, n + 1):
#        if n % d == 0:
#            print(d)
# factor(36)

def getTotalX(a, b):
    fact = []
    for x in range(max(a), min(b) + 1):
        if all(x % i == 0 for i in a):
            if all(i % x == 0 for i in b):
                fact.append(x)
    return len(fact)

print(getTotalX([2,4],[16,32,96]))
print(getTotalX([2,6],[24, 36]))


