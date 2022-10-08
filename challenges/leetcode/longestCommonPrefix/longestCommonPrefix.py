class Solution: 
    def longestCommonPrefix(self, strs): 
        if len(strs) == 0:
            return ""
        if len(strs) == 1: 
            return strs[0]
        prefix = strs[0]
        for i in range(0, len(strs)):
            while strs[i].find(prefix) != 0:
                print("prefix: " + prefix)
                prefix = prefix[0:len(prefix)-1]
                if len(prefix) == 0:
                    return ""
        return prefix
    
    def rLCP(self, strs, prefix=""):
        if len(strs) == 0: 
            return ""
        if len(strs) == 1: 
            return strs[0]
        
        for i in range(0, len(strs)):
            if strs[i].find(prefix) != 0:
                prefix = self.rLCP(strs, prefix[0:len(prefix) - 1])
                if len(prefix) == 0:
                    return ""
            else: 
                return prefix



if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))
    print(solution.longestCommonPrefix(["dog","racecar","car"]))

    print(solution.rLCP(["flower","flow","flight"]))