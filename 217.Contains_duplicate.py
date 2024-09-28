# Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

#solution with Hashmap
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        for num in nums:
            if(num not in dup.keys()):
                dup[num] = 1
            else:
                dup[num] += 1
        for rep in dup.values():
            if(rep>1):
                return True
            
        else:
            return False

#solution with set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False