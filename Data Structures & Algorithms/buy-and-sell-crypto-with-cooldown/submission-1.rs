use std::cmp::max;

// struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let n = prices.len();
        if n == 0 { return 0; }

        let mut dp = vec![vec![-1; 2]; n];

        Self::dfs(0,1, &prices, &mut dp)
    }
    fn dfs(i: usize, buying: usize, prices: &Vec<i32>, dp: &mut Vec<Vec<i32>>)-> i32 {
        if i >= prices.len(){ return 0; }
        if dp[i][buying] != -1 {
            return dp[i][buying];
        }

        let cooldown = Self::dfs(i+1, buying, prices, dp);

        if buying ==1 {
            let buy = Self::dfs(i+1, 0, prices, dp) - prices[i];
            dp[i][buying] = max(buy, cooldown);
        } else {
            let sell = Self::dfs(i+2, 1, prices, dp) + prices[i];
            dp[i][buying] = max(sell, cooldown);
        }
        dp[i][buying]
    }
}
