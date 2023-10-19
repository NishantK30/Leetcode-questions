class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        mid = (start + end)>>1

        while(start<=end):
            
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                end = mid - 1
            else:
                start = mid + 1
            
            mid = (start + end)>>1
            
        return -1