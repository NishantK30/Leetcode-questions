'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.'''


from math import floor

def findMedianSortedArrays( nums1: list[int], nums2: list[int]) -> float:
        mergedarr = []
        l = r = 0   
        n1,n2 = len(nums1), len(nums2)

        while(l<n1 and r<n2):
            if nums1[l] <= nums2[r]:
                mergedarr.append(nums1[l])
                l += 1
            else:
                mergedarr.append(nums2[r])
                r += 1
        
        while l < n1:
            mergedarr.append(nums1[l])
            l += 1
        
        while r < n2:
            mergedarr.append(nums2[r])
            r += 1
        
        n3 = len(mergedarr)
        if n3 % 2 != 0:
            median = mergedarr[(int(floor(n3/2)))]
        else:
            median = (mergedarr[int(n3/2)] + mergedarr[int(n3/2)-1]) / 2
        
        return median