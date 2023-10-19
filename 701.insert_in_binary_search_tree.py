class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            root = TreeNode(val)
            return root
        if val > root.val:
            root.right = self.insertIntoBST(root.right,val)
    
        elif val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        
        return root