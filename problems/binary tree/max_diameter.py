# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0

        def dfs(node:Optional[TreeNode]) -> int:
            
            nonlocal diameter
            if not node:
                return 0

            ## Recurse through the tree
            left_subtree = dfs(node.left)
            right_subtree = dfs(node.right)

            local_diameter = left_subtree+right_subtree
            diameter = max(diameter,local_diameter)

            return max(left_subtree,right_subtree) + 1
        dfs(root)
        return diameter

        


