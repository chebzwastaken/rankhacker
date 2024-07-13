#
# @lc app=leetcode id=1717 lang=python3
#
# [1717] Maximum Score From Removing Substrings
#
# https://leetcode.com/problems/maximum-score-from-removing-substrings/description/
#
# algorithms
# Medium (47.22%)
# Likes:    1346
# Dislikes: 111
# Total Accepted:    127.6K
# Total Submissions: 201.8K
# Testcase Example:  '"cdbcbbaaabab"\n4\n5'
#
# You are given a string s and two integers x and y. You can perform two types
# of operations any number of times.
# 
# 
# Remove substring "ab" and gain x points.
# 
# 
# For example, when removing "ab" from "cabxbae" it becomes
# "cxbae".
# 
# 
# Remove substring "ba" and gain y points.
# 
# For example, when removing "ba" from "cabxbae" it becomes
# "cabxe".
# 
# 
# 
# 
# Return the maximum points you can gain after applying the above operations on
# s.
# 
# 
# Example 1:
# 
# 
# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5
# points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4
# points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points
# are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are
# added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.
# 
# Example 2:
# 
# 
# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# 1 <= x, y <= 10^4
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove(s, sub, points):
            stack = []
            for c in s:
                stack.append(c)
                if len(stack) >= 2 and stack[-2:] == list(sub):
                    stack.pop()
                    stack.pop()
                    points += points
            return ''.join(stack), points

        if x < y:
            s, x, y = s[::-1], y, x

        s, points = remove(s, 'ab', x)
        s, points = remove(s, 'ba', y)

        return points
# @lc code=end

