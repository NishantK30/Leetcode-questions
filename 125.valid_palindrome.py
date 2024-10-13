"""
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

#python solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #clean_s = ''.join(char for char in s if char.isalnum()).lower()
        clean_s = ''.join(filter(str.isalnum, s)).lower()
        s_len = len(clean_s)
        top = s_len-1
        bottom = 0
        if s_len == 0:
            return True
        while(top>bottom):
            if(clean_s[bottom]!=clean_s[top]):
                return False
            top-=1
            bottom +=1
            
        return True

#cpp soltuion
"""
class Solution {
public:
    bool isPalindrome(string s) {
       int start=0;
       int end=s.size()-1;
       while(start<=end){
           if(!isalnum(s[start])){start++; continue;}
           if(!isalnum(s[end])){end--;continue;}
           if(tolower(s[start])!=tolower(s[end]))return false;
           else{
               start++;
               end--;
           }
       }
       return true;
}
};
"""