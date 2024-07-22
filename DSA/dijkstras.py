import heapq


def make_graph():
    # identical graph as the YouTube video: https://youtu.be/_lHSawdgXpI
    # tuple = (cost, to_node)
    return {
        'A': [(4, 'B'), (2, 'C')],
        'B': [(3, 'C'), (1, 'E'), (2, 'D')],
        'C': [(1, 'B'), (4, 'D'), (5, 'E')],
        'D': [],
        'E': [(1, 'D')],
    }


def func(G, start='A'):
    # Step 1: Initialization
    

    # Initialize all distances to infinity
    # Distance to the start node is 0 and mark it as visited
    # Push the start node with distance 0 onto the heap


    # Step 2: Main Loop: (clue what should not exist for us to return the shortest paths?)
    # Pop the node with the smallest distance
    #  Check all edges connected to 'node'
     
    
    # If 'to_node' is not visited and the new distance is shorter
    # Update the shortest path to 'to_node'
    # Push the new distance to 'to_node' onto the heap
    
    # Step 3: Completion return the shortest paths

    shortest_paths = {}
    visited = set()
    heap = []

    for node in G.keys():
        shortest_paths[node] = float("inf")
    
    shortest_paths[start] = 0
    visited.add(start)
    heapq.heappush(heap, (shortest_paths[start], start))

    while heap:
        (distance, node) = heapq.heappop(heap)

        for (cost, to_node) in G[node]:
            if to_node not in visited and distance + cost < shortest_paths[to_node]:

                shortest_paths[to_node] = distance + cost 

                heapq.heappush(heap, (shortest_paths[to_node], to_node))
    
    return shortest_paths






def main():
    G = make_graph()
    start = 'A'

    # shortest_paths = dijkstras(G, start)
    # print(f'Shortest path from {start}: {shortest_paths}')
    shortest_paths_using_heap = func(G, start)
    print(f'Shortest path from {start} using heap: {shortest_paths_using_heap}')


main()