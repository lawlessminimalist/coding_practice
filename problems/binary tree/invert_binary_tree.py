# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List,Optional

class Solution:

    """ 
        Recursively swap the ordering of the left and right children in each subtree    
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case for recursion
        if root is None:
            return root

        tmp = root.left
        root.left = root.right
        root.right = tmp
        if root.left is not None:
            self.invertTree(root.left)
        if root.right is not None:
            self.invertTree(root.right)
        return root