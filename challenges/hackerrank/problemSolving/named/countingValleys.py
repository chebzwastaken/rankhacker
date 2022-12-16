def countingValleys(steps, path):
    valleys = 0
    level = 0
    for step in path:
        if step == 'U':
            level += 1
            if level == 0:
                valleys += 1
        else:
            level -= 1
    return valleys

print(countingValleys(8, 'UDDDUDUU'))
