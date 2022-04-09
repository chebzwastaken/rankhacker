def sockMerchant(n, ar):
    pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if ar[i] == ar[j]:
                pairs += 1
                ar[j] = 0
    return pairs