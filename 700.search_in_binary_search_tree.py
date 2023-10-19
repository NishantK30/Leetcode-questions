class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        if root.val == val:
            return root

        if root.val > val:
            return Solution.searchBST(self,root.left,val)

        if root.val < val:
            return Solution.searchBST(self,root.right,val)