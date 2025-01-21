'''Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false'''


def checkInclusion( s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1_count = {}
        s2_count = {}

        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i],0)
            s2_count[s2[i]] = 1 + s2_count.get(s2[i],0)
        
        if s1_count == s2_count:
            return True
        
        left = 0
        for right in range(len(s1),len(s2)):
            s2_count[s2[right]] = 1 + s2_count.get(s2[right],0)
            s2_count[s2[left]] -= 1

            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]
            
            left += 1

            if s1_count == s2_count:
                return True
                
        return False
            
            
        
s2 = "dcda"
s1 = "adc"
print(checkInclusion(s1, s2))