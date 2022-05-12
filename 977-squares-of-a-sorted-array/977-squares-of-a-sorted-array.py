import math
class Solution(object):
    def sortedSquares(self, nums):
        a = sorted(list(map(lambda a : a * a, nums)))
        return (a)