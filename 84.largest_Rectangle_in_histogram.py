'''iven an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4'''


def largestRectangleArea( heights: list[int]) -> int:
        #improvement on commented code below
        #becuause we dont use enumerate method and also
        #elimante some condition that can be handled before 
        #while loop
        stack = []

        stack.append((0,heights[0]))
        largestArea = 0
        for i in range(1, len(heights)):
            curr = heights[i]
            start, prevHeight = stack[-1]
            
            if prevHeight < curr:
                stack.append((i, curr))
            elif prevHeight == curr:
                continue
            else:
                while stack and stack[-1][1] > curr:          
                    area = (i-stack[-1][0])*stack[-1][1]
                    start = stack[-1][0]
                    stack.pop()
                    largestArea = max(largestArea, area)
                   
                stack.append((start, curr))
            
        #print(stack)
        while stack:
            start, prevHeight = stack[-1]
            if start == len(heights)-1:
                largestArea = max(largestArea, prevHeight)
            else:
                area = (len(heights) - start) * prevHeight #if we didn't pop it yet that means it reached till the end
                largestArea = max(largestArea,area)
            stack.pop()

        return largestArea
        # maxArea = 0
        # stack = [] # pair: (index,height)

        # for i, h in enumerate(heights):
        #     start = i
        #     while stack and stack[-1][1]>h:
        #         index, height = stack.pop()
        #         maxArea = max(maxArea, height * (i - index))
        #         start = index
            
        #     stack.append((start,h))
        
        # for i,h in stack:
        #     maxArea = max(maxArea, h * (len(heights) - i))
        
        # return maxArea
        
        
