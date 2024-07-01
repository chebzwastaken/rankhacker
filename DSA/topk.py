import heapq 
from collections import Counter

def topk(nums, k):
    # Step 1: Count the frequency of each element
    frequency_map = Counter(nums)

    print(frequency_map)

    # Step 2: Use a min-heap to keep track of the top k elements
    # Heap stores tuples of (-frequency, element) to make a max-heap using min-heap
    heap = []
    for num, freq in frequency_map.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    # Step 3: Extract elements from the heap
    top_k_elements = []
    while heap:
        top_k_elements.append(heapq.heappop(heap)[1])

    return top_k_elements[::-1] 