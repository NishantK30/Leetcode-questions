class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lst = []
        dict = {}

        def find_mode(root):
            if root is None:
                return None
            
            if root.val not in dict:
                dict[root.val]=1
            else:
                dict[root.val]+=1

            find_mode(root.left)
            find_mode(root.right)

            return dict
        
        find_mode(root)
        mode_list = max(list(dict.values()))
        for key,val in dict.items():
            if val == mode_list:
                lst.append(key)

        return lst