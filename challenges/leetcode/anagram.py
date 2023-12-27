def anagram(t, s):
    """Check if two strings are anagrams."""
    if len(s) != len(t):
        return False
    
    s_map = {n:s.count(n) for n in s }

    for i in t:
        if i not in s_map.keys() or t.count(i) != s_map[i]:
            return False
    return True


arr = [[1,2,3,4,5, 7], [1,2,3,4,5,6]]

# add a new element to the array at the end
# add a new element to a subarray containing the value 7
arr[-1].append("a")

print(arr)