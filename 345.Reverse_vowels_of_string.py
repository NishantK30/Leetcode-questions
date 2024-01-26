'''Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases,
more than once.'''



class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")
        s = list(s)
        i = 0
        j = len(s)-1

        while i < j:
            if s[i] in vowels and s[j] in vowels:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i+=1
                j-=1

            elif s[i] in vowels:
                j -= 1
            
            elif s[j] in vowels:
                i += 1

            else:
                i += 1
           
        return "".join(s)
        