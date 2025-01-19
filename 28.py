'''Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.'''


def strStr( haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        if h<n: return -1
        if h ==n:
            return 0 if haystack==needle else -1

        for l in range(h):
            if haystack[l:l+n] == needle:
                return l
            
        return -1
    
    
haystack = "mississippi"
needle = "issipi"
print(strStr(haystack, needle))