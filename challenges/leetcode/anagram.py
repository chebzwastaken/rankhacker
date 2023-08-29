def anagram(t, s):
    """Check if two strings are anagrams."""
    if len(s) != len(t):
        return False
    
    s_map = {n:s.count(n) for n in s }

    for i in t:
        if i not in s_map.keys() or t.count(i) != s_map[i]:
            return False
    return True