class Solution(object):
    def searchInsert(self, nums, target):
        i = 0
        while i < len(nums):
            if nums[i] >= target:
                return i
            i += 1
        return len(nums)

class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
            