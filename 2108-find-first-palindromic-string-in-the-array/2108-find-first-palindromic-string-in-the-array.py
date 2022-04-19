class Solution(object):
    def is_palindrome(self, word):
        if (word[::-1] == word):
            return True
        else:
            return False
    def firstPalindrome(self, words):
        for i in words:
            if self.is_palindrome(i):
                return (i)
        return ""