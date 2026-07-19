class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = str(x)
        num = res[::-1]
        if x < 0:
            return False
        elif res == num:
            return True
        return False