'''Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"'''

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''if set(word1) != set(word2):
            return False
        counter1 = {}
        counter2={}
        for i in word1:
            counter1[i] = counter1.get(i,0)+1
        
        for i in word2:
            counter2[i] = counter2.get(i,0)+1


        return sorted(list(counter1.values())) == sorted(list(counter2.values()))'''
        unique_char = set(word1)
        f1, f2 = [], []

        if len(word1) == len(word2):
            for char in unique_char:
                f1.append(word1.count(char))
                f2.append(word2.count(char))
            
            f1.sort()
            f2.sort()

            return f1 == f2
        else:
            return False
        
