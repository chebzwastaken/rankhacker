def divisiblesumpairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(n):
            if i < j and (ar[i] + ar[j]) % k == 0:
                count += 1
    return count


n, k = map(int, input().split())
ar = list(map(int, input().split()))
print(divisiblesumpairs(n, k, ar))



















