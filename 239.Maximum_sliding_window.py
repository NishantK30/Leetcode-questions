'''You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]'''

import collections


def maxSlidingWindow( nums: list[int], k: int) -> list[int]:
        output = []
        q = collections.deque()
        l=r=0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #remove left from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
        
        # max_sub = []
        # start = 0
        # end = k if k <= len(nums) else len(nums)
        # while( end <= len(nums)):
        #     max_ = float('-infinity')
        #     for i in range(start,end):
        #         max_ = max(max_,nums[i])
            
        #     max_sub.append(max_)
        #     start += 1
        #     end += 1
        
        # return max_sub
    
nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(maxSlidingWindow(nums, k))