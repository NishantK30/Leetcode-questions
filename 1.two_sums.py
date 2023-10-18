class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = { }
        for curr_indx in range(len(nums)):
            curr_num = nums[curr_indx]
            diff = target - curr_num

            if diff in visited:
                visited_indx = visited[diff]
                return [visited_indx,curr_indx]
            
            else:
                visited[curr_num] = curr_indx 