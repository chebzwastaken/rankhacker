def twoSumOne(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSumTwo( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i in range(len(nums)):
        if nums[i] in d:
            return [d[nums[i]], i]
        else:
            d[target - nums[i]] = i

print(twoSumTwo([2, 7, 11, 15], 9)) 
# print(twoSumOne([2, 7, 11, 15], 9))
