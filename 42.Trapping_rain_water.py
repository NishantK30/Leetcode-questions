'''Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9'''



class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_trapped = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1

        return water_trapped



        
    
        #approach with more space complexity
        # n = len(heights)
        # max_left = [0]*n
        # left = 0
        # for i in range(n):
        #     max_left[i] = left
        #     if heights[i]>left:
        #         left = heights[i]

        # max_right = [0]*n
        # right = 0
        # for i in range(n-1,-1,-1):
        #     max_right[i] = right
        #     if heights[i] > right:
        #         right = heights[i]

        # trapped_water = 0
        # for i,height in enumerate(heights):
        #     water = min(max_left[i],max_right[i]) - height
        #     if water>0:
        #         trapped_water+=water
        # return trapped_water

        #faster than keeping track of maxleft and right arrays
        #if not heights:
        #    return 0
#
        #left,right = 0,len(heights)-1
        #max_left,max_right = heights[left],heights[right]
#
        #res = 0
        #while(left<right):
        #    if max_left<=max_right:
        #        left += 1
        #        max_left = max(heights[left],max_left)
        #        res += max_left - heights[left]
        #        
        #    else:
        #        right-=1
        #        max_right = max(heights[right],max_right)
        #        res += max_right - heights[right]
        #        
#
        #return res
    

heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(heights))