class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        str_list = []
        i =0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                str_list.append(word1[i])
            if i < len(word2):
                str_list.append(word2[i])
            
            i += 1

        merge_str = ''.join(str_list)

        return merge_str