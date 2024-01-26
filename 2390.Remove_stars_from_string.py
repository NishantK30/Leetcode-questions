'''You are given a string s, which contains stars *.
In one operation, you can:
Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.
Note:
1.The input will be generated such that the operation is always possible.
2.It can be shown that the resulting string will always be unique.'''



class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if s[i] != '*':
                stack.append(s[i])
            else:
                stack.pop()
        
        return "".join(stack)
        
        