class Solution(object):
    def reverse(self, x):
        sign = 0
        if x <= 0:
            if x == 0:
                return 0
            sign = 1
        s = str(x)
        s = s[::-1]
        s = s.rstrip('-')
        s = s.strip('0')
        negative = '-'
        if sign == 1:
            negative += s
            if int(negative) < (-2 ** 31) or int(negative) > (2 ** 31):
                return 0
            return negative
        if int (s) < (-2 ** 31) or int(s) > (2 ** 31):
                return 0
        return s
        