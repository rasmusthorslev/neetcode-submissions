# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(node):
            nonlocal balanced
            left_height = dfs(node.left) if node.left else 0
            right_height = dfs(node.right) if node.right else 0
            if abs(left_height-right_height) > 1:
                balanced = False
            return 1+max(left_height,right_height)
        if root: dfs(root)
        return balanced
