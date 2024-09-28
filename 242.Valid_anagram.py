# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

#python solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        
        return sorted(s)==sorted(t)
    
#cpp solution
# 1 sorting string
# class Solution {
# public:
#     bool isAnagram(string s, string t) {
#         if(s.length()!=t.length()) return false;
#         sort(s.begin(),s.end());
#         sort(t.begin(),t.end());
#         return s == t;
#     }
# };

# 2 map
# class Solution {
# public:
#     bool isAnagram(string s, string t) {
#         unordered_map<char,int>mp ;
#         if(s.size()!=t.size())
#         return 0 ;
#         for(int i=0;i<s.size();i++)
#         {
#             mp[s[i]]++ ;
#         }
#         for(int i=0;i<t.size();i++)
#         {
#             mp[t[i]]-- ;
#         }

#         for(auto i:mp)
#         if(i.second!=0)
#         return 0 ;

#         return 1 ;
        
        
#     }
# };    