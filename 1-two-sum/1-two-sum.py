
class Solution(object):
    
    def twoSum(self, nums, target):
        i = 0
        result = []
        while i < len(nums):
            j = len(nums) - 1
            while j != i:
                if nums[i] + nums[j] == target  and i != j:
                    result.append(i)
                    result.append(j)
                    return result
                j -= 1
            i += 1