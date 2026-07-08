class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minbuy = prices[0]

        for price in prices:
            max_profit = max(max_profit, price - minbuy)
            minbuy = min(minbuy, price)

        return max_profit