class Solution(object):
    def isPalindrome(self, s):
        r = [i.lower() for i in s if i.isalnum()]
        r = ''.join(r)
        print(r)
        if r == r[::-1]:
            return True
        else:
            return False
        
        