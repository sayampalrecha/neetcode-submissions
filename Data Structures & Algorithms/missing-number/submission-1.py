class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        valid_sum = int((1+n) * n /2)
        return valid_sum - sum(nums)

        