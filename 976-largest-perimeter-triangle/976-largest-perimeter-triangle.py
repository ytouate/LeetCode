class Solution(object):
    def isValid(self, a, b, c):
        return a + b > c
    def largestPerimeter(self, nums):
        t = list((sorted(nums)))
        i = len(t) - 1
        while i >= 2:
            if t[i] < t[i - 1] + t[i - 2]:
                return (t[i] + t [i-1] + t[i - 2])
            i -= 1
        return 0
            