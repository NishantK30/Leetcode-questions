class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder_list = []
        def inorder(node):
            if node:
                inorder(node.left)
                inorder(node.right)
                inorder_list.append(node.val)
        
        inorder(root)
        return inorder_list