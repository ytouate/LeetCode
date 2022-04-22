import math
class Solution(object):
    def sortedSquares(self, nums):
        left = 0
        temp = []
        right = len(nums) - 1
        j = len(nums) - 1
        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                temp.insert(0, nums[left] * nums[left])
                left += 1
                j -= 1
            else:
                temp.insert(0, nums[right] * nums[right])
                right -= 1
                j -= 1
        return temp
            