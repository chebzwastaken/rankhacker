class Stackfish: 
    def win_garen(width, height, position):
        count = 0
        win_garen = False
        for i in range(0, len(position) - 1):
            if position[i] == 0 and position[i-1] == 1 or 2:
                if position[i+1] == position[i-1]:
                    count += 1
        if count == 2: 
            win_garen = True
        print(count)
        print(win_garen)
        return win_garen

Stackfish.win_garen(4, 2, [ 1, 1, 0, 1, 2, 2, 0, 2 ])

Stackfish.win_garen(4, 5, [ 1, 2, 2, 1, 1, 2, 2, 0, 1, 1, 2, 0, 2, 0, 1, 0, 0, 0, 0, 0 ])

# [ 1, 1, 0, 1,
#   2, 2, 0, 2 ]

# [ 1, 2, 2, 1,
#   1, 2, 2, 0,
#   1, 1, 2, 0,
#   2, 0, 1, 0,
#   0, 0, 0, 0 ]