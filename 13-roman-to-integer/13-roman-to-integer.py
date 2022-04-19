class Solution(object):
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    r = 0
    def romanToInt(self, str):
        res = 0
        i = 0
        while (i < len(str)):
            s1 = self.d[str[i]]
            if (i + 1 < len(str)):
                s2 = self.d[str[i + 1]]
                if (s1 >= s2):
                    res = res + s1
                    i = i + 1
                else:
                    res = res + s2 - s1
                    i = i + 2
            else:
                res = res + s1
                i = i + 1
        return res
        