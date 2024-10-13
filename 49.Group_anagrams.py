"""Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other."""

#python solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:            
        mp = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            mp[sorted_word].append(word)
        
        return list(mp.values())
    
#cpp solution
"""
    class Solution {
    public:
        vector<vector<string>> groupAnagrams(vector<string>& strs) {
            unordered_map<string,vector<string>> mp;
            for(auto i: strs){
                string word = i;
                sort(word.begin(),word.end());
                mp[word].push_back(i);
            }
            vector<vector<string>> result;
            for(auto i: mp){
                result.push_back(i.second);
            }
            return result;
            
        }
    };
"""