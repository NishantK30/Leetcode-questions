'''
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''
import heapq
#sol 1
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums_r = []

        for num in nums:
            heapq.heappush(nums_r, num)
            if (len(nums_r) > k):
                heapq.heappop(nums_r)
        
        return nums_r[0]

#sol 2
#use quick select
