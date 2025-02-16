def maxSlidingWindow( nums: list[int], k: int) -> list[int]:
        max_sub = []
        start = 0
        end = k if k <= len(nums) else len(nums)
        while( end <= len(nums)):
            max_ = float('-infinity')
            for i in range(start,end):
                max_ = max(max_,nums[i])
            
            max_sub.append(max_)
            start += 1
            end += 1
        
        return max_sub
    
nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(maxSlidingWindow(nums, k))