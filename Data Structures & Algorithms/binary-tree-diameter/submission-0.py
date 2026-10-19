# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal diameter
            left_height = dfs(node.left) if node.left else 0
            right_height = dfs(node.right) if node.right else 0
            diameter = max(diameter, left_height+right_height)
            return 1+max(left_height,right_height)
        
        dfs(root)
        return diameter