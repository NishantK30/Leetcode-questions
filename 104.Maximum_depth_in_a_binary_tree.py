'''Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the 
longest path from the root node down to the farthest leaf node.

 Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right'''
         
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))