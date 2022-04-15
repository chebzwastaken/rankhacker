def getMoneySpent(keyboards, drives, b):
    # Write your code here
    max_price = -1
    for i in keyboards:
        for j in drives:
            if i + j <= b and i + j > max_price:
                max_price = i + j
    return max_price