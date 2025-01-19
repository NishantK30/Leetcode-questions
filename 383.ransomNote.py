'''Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true'''



from collections import Counter

def canConstruct( ransomNote: str, magazine: str) -> bool:
    
    
        count = Counter(magazine)
        for char in ransomNote:
            if count[char] == 0:
                return False
            count[char] -= 1
        return True
    
        # for char in ransomNote:
        #     if char not in magazine:
        #         return False
        #     magazine = magazine.replace(char, '', 1)
        # return True
    
       #  noteCounter = Counter(ransomNote)
       #  magCounter = Counter(magazine)
        
       #  for key,value in noteCounter.items():
       #      if key not in magCounter:
       #          return False
                
       #      elif value > magCounter[key]:
       #          return False
            
       #  return True
            
            
ransomNote ="fihjjjjei"
magazine = "hjibagacbhadfaefdjaeaebgi"
print(canConstruct(ransomNote, magazine))