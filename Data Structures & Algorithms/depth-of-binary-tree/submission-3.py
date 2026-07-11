# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node.left != None and node.right != None:
                return 1+ max(dfs(node.left), dfs(node.right))
            if node.left != None:
                return 1+  dfs(node.left)
            if node.right != None:
                return 1+ dfs(node.right)
            return 0

        if root != None:
            return 1+dfs(root)
        else:
            return 0
    
        