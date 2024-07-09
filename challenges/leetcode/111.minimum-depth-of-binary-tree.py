#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (48.44%)
# Likes:    7279
# Dislikes: 1310
# Total Accepted:    1.2M
# Total Submissions: 2.5M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^5].
# -1000 <= Node.val <= 1000
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_height = self.minDepth(root.left) + 1
        right_height = self.minDepth(root.right) + 1
        if left_height == 1 and right_height > 1:
            return right_height
        if right_height == 1 and left_height > 1:
            return left_height
        return min(left_height, right_height)
        

# @lc code=end

