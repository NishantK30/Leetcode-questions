class Solution:
    def maxArea(self, height: list[int]) -> int:
        LB = 0
        HB = len(height)-1
        max_area = 0
        while (LB != HB):
            breadth = HB - LB
            if height[LB] > height[HB]:
                lenght = height [HB]
                HB -=1
            else:
                lenght = height[LB]
                LB +=1
            
            area = lenght * breadth
            if area>max_area:
                max_area = area
                
        return max_area
        