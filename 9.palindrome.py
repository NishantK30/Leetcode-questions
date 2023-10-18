class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return 0
        y=0
        t = x
        while(t>0):
            y = y*10 + t%10
            t= t//10
        
        return x==y