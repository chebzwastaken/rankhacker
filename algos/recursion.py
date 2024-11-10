def decrement(number: int):
    print(number) 
    if number <= 0: 
        return 
    else: 
        decrement(number - 1)

decrement(100000)
