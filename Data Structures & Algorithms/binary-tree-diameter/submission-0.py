# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        def dfs(node):
            if node != None:
                left = dfs(node.left)
                right = dfs(node.right)
                nonlocal maxi 
                maxi = max(left+right, maxi)
                return 1 + max(left, right)
            else:
                return 0
        
        dfs(root)
        return maxi