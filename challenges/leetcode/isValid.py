class Solution: 
    def isValid(self, s:str) -> bool:
        stack = []
        
        for c in s:
            print(c, stack)
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif not stack or c != stack.pop():
                return False
        return not stack

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("{{}}()[[]]"))