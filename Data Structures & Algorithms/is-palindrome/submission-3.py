class Solution:
    def isPalindrome(self, s: str) -> bool:
        # solution 1 here 
        new = ""

        for c in s:
            if c.isalnum():
                new += c.lower()
        return new == new[::-1]

        