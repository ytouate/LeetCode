import math
class Solution(object):
    def sortedSquares(self, nums):
        left = 0
        temp = []
        right = len(nums) - 1
        j = len(nums) - 1
        while left <= right:
            if abs(nums[left]) * abs(nums[left]) > abs(nums[right]) * abs(nums[right]):
                temp.insert(0, abs(nums[left]) * abs(nums[left]))
                left += 1
                j -= 1
            else:
                temp.insert(0, abs(nums[right]) * abs(nums[right]))
                right -= 1
                j -= 1
        return temp
            