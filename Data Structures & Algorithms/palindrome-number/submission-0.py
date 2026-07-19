class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num = int(str(abs(x))[::-1])

        if reversed_num == x:
            return True
        else: return False