'''Given an array nums of distinct integers, return all the possible 
permutations
. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]'''


def permute( nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res,sol=[],[]

        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
            
        backtrack()
        return res 
    
        # This is faster than backtracking somehow
        # res = [[]]
        # for num in nums:
        #     new_res = []
        #     n = len(res[0])
        #     for item in res:
        #         for i in range(n + 1):
        #             new_res.append(item[:i] + [num] + item[i:])
        #     res = new_res
        # return res
