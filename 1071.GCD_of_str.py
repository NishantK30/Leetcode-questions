'''For two strings s and t, we say "t divides s" if and only if s = t + ... + t 
(i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"  '''

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1 = len(str1)
        len2 = len(str2)
        min_strlen = min(len1,len2)
        len_gcd = 0
        for i in range(min_strlen, 0, -1):
            if len1 % i == 0 and len2 % i == 0:
                len_gcd = i
                break

        str1_gcd = len1 // len_gcd
        str2_gcd = len2 // len_gcd

        if ((str2[:len_gcd])*str2_gcd) != str2:
            return ''
        
        str_gcd = ''

        for i in range(str1_gcd):
            str_gcd += str2[:len_gcd]

        return str2[:len_gcd] if str_gcd == str1 else ''
        

        
        