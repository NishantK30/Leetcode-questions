'''Given an integer array nums, move all 0's 
to the end of it while maintaining 
the relative order of the non-zero elements.
Note that you must do this in-place without 
making a copy of the array.'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1