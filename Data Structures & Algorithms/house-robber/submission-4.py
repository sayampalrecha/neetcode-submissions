class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up tabulation approach 
        # time and space = O(n)
        # case1 = [2,3,2,5,1]

        n = len(nums)
        if n == 1:
                return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        # created cache here called memo
        memo = {0:nums[0], 1:max(nums[0],nums[1])}

        def helper(i):
            if i in memo:
                return memo[i]
            else:
                memo[i]= max(nums[i]+helper(i-2), helper(i-1))
                return memo[i]
        return helper(n-1)
        