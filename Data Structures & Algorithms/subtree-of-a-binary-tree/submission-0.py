# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None and node2:
                return False
            elif node1 and node2 is None:
                return False
            elif node1.val != node2.val:
                return False
            return compare(node1.left, node2.left) and compare(node1.right, node2.right)
        def dfs(root):
            if root is None:
                return False
            if compare(root, subRoot):
                return True
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)
