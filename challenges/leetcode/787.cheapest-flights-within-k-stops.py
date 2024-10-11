#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
#
# algorithms
# Medium (39.41%)
# Likes:    9893
# Dislikes: 413
# Total Accepted:    585.1K
# Total Submissions: 1.5M
# Testcase Example:  '4\n[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]\n0\n3\n1'
#
# There are n cities connected by some number of flights. You are given an
# array flights where flights[i] = [fromi, toi, pricei] indicates that there is
# a flight from city fromi to city toi with cost pricei.
# 
# You are also given three integers src, dst, and k, return the cheapest price
# from src to dst with at most k stops. If there is no such route, return
# -1.
# 
# 
# Example 1:
# 
# 
# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
# src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and
# has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because
# it uses 2 stops.
# 
# 
# Example 2:
# 
# 
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k
# = 1
# Output: 200
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and
# has cost 100 + 100 = 200.
# 
# 
# Example 3:
# 
# 
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k
# = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost
# 500.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 10^4
# There will not be any multiple flights between two cities.
# 0 <= src, dst, k < n
# src != dst
# 
# 
#

# @lc code=start
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        
        G = {}
        for (from_node, to_node, cost) in flights:
            if from_node not in G:
                G[from_node] = {to_node:cost}
            else:
                G[from_node][to_node] = cost

        shortest_paths = {}
        heap = []

        heapq.heappush(heap, (0,(src,0)))

        while heap and len(shortest_paths) != n:

            cost, (node, stops) = heapq.heappop(heap)

            if node in shortest_paths:
                if stops < shortest_paths[node]:
                    shortest_paths[node] = stops
                else:
                    continue
            else:
                shortest_paths[node] = stops

            if node == dst:
                return cost

            if node in G:
                for next_node, next_cost in G[node].items():
                    if n not in shortest_paths and (stops < k or next_node == dst):
                        heapq.heappush(heap, (cost + next_cost, (next_node, stops + 1)))

        return -1

    # @lc code=end