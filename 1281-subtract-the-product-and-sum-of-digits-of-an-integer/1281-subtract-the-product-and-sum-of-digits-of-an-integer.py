class Solution(object):
    def subtractProductAndSum(self, n):
        n = str(n)
        sum = 1
        add = 0
        for i in n:
            sum *= int(i)
            add += int(i)
        return sum - add
        