'''l ,r = 0, len(nums)-1

        while(l<=r):
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid-1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1'''


def search(nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while (l <= r):
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid-1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

nums = [4, 5, 6, 7,0,1,2]
target = 0
print(search(nums, target))
