class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        padded_nums = [1]+nums+[1]
        n = len(padded_nums)

        dp = [[0]*n for _ in range(n)]

        for length in range(1, len(nums)+1):
            for i in range(n - length -1):
                j = i + length + 1

                for k in range(i+1, j):
                    coins = padded_nums[i]*padded_nums[k]*padded_nums[j]
                    total = dp[i][k] + dp[k][j] + coins
                    dp[i][j] = max(dp[i][j], total)
        return dp[0][n-1]