class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder_list = []
        def inorder(node):
            if node:
                inorder(node.left)
                inorder_list.append(node.val)
                inorder(node.right)
        
        inorder(root)
        return inorder_list