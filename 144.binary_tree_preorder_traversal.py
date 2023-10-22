class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder_list = []
        def inorder(node):
            if node:
                inorder_list.append(node.val)
                inorder(node.left)
                inorder(node.right)
        
        inorder(root)
        return inorder_list