import math 
def primefinder(N):
    arr = list(range(2, N+1))
    count = 0
    k = arr[count]
    while k <= math.sqrt(N) :
        for i in range(k, N):
            print(arr)
            if (i*k) in arr:
                arr.remove(i*k)
            elif i > N / k:
                break
        count+=1
        k = arr[count]
    print(arr, arr[-1])
    return arr[-1]
    
def is_prime(n):
    if n > 1:
        for i in range(2, n//2):
            if (n % i) == 0:
                print(n, "is not a prime number")
                break
            else:
                print(n, "is a prime number")
    else:
        print(n, "is not a prime number")

def first_prime(n):
    for i in range(n):
        for i in range(2, (2 ** n - 1) // 2):
            if (((2 ** n) - 1) % i) == 0:
                print(f"2^{n} - 1 is not a prime number")
                break
            else:
                print(f"2^{n} - 1 is a prime number")
    else:
        print(f"2^{n} - 1 is not a prime number")


# wilson theorem
def wilson(n):
    return 1 + sum([
        math.floor(pow(n/sum([
            math.floor(pow(math.cos(math.pi * (math.factorial(j - 1) + 1) / j), 2))
            for j in range(1, i + 1)
        ]), 1/n))
        for i in range(1, pow(2, n) + 1)
    ])





if __name__ == '__main__':
    [print(wilson(i)) for i in range(1, 10+1)]