class Solution(object):
    def countOdds(self, low, high):
        count = 0
        if low % 2 == 0:
            low += 1
        if high % 2 == 0:
            high -= 1
        count = ((high - low) / 2) + 1
        return count
        
        