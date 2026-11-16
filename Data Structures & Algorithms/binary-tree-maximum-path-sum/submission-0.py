# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return root.val
        
        max_triangle = -float("inf")
    
        def dfs(node):
            nonlocal max_triangle
            if node.left is None and node.right is None:
                max_triangle = max(node.val, max_triangle)
                return node.val
            right, left = 0, 0    
            if node.right:
                right = max(dfs(node.right), 0)
            if node.left:
                left = max(dfs(node.left), 0)
    
            max_triangle = max(left + node.val + right, max_triangle)

            return node.val + max(right,left)
        
        return max(dfs(root), max_triangle)