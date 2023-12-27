from functools import reduce
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in freq[:k]]

    


# how to take nums[i] and sum the rest 

# Path: challenges/leetcode/sumrest.py
def sumrest(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return [sum(nums[:i] + nums[i+1:]) for i in range(len(nums))]

# how does sum work?
def productsum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return [reduce(lambda x, y: x*y, nums[:i] + nums[i+1:]) for i in range(len(nums))]






