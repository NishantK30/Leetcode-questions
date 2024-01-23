class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min(nums)
        max_num = max(nums)

        for i in range(min_num,0,-1):
            if min_num % i == 0 and max_num % i == 0:
                return i