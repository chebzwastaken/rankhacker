#
# @lc app=leetcode id=1190 lang=python3
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
#
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
#
# algorithms
# Medium (66.50%)
# Likes:    2755
# Dislikes: 116
# Total Accepted:    210.4K
# Total Submissions: 293.6K
# Testcase Example:  '"(abcd)"'
#
# You are given a string s that consists of lower case English letters and
# brackets.
# 
# Reverse the strings in each pair of matching parentheses, starting from the
# innermost one.
# 
# Your result should not contain any brackets.
# 
# 
# Example 1:
# 
# 
# Input: s = "(abcd)"
# Output: "dcba"
# 
# 
# Example 2:
# 
# 
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is
# reversed.
# 
# 
# Example 3:
# 
# 
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally,
# the whole string.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 2000
# s only contains lower case English characters and parentheses.
# It is guaranteed that all parentheses are balanced.
# 
# 
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ')':
                tmp = []
                while stack and stack[-1] != '(':
                    tmp.append(stack.pop())
                stack.pop()
                stack += tmp
            else:
                stack.append(c)
        return ''.join(stack)
# @lc code=end

