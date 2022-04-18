def denseRanker(ranked): 
    ranked = sorted(ranked, reverse=True)
    ranking = [1]
    place = 1
    for i in range(len(ranked) - 1):   
        if ranked[i] !=  ranked[i + 1]:
            place += 1 
        # print(ranked[i], ranked[i + 1], place)  
        ranking.append(place)
    return ranking

            
                


def climbingLeaderboard(ranked, player):

    ranked = sorted(list(set(ranked)))
    n = len(ranked)
    i = 0
    result = []
    for score in player:
        while i < n and ranked[i] <= score:
            i += 1
        result.append(n - i + 1) 
    return result
            

        
    


print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
# print(climbingLeaderboard([100, 90, 90, 80], [70, 80, 105]))

