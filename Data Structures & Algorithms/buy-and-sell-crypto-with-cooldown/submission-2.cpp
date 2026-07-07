#include <vector>
#include <algorithm>

class Solution {
private:
    std::vector<std::vector<int>> dp;
    std::vector<int> prices_list;

public:
    int maxProfit(std::vector<int>& prices) {
        int n = prices.size();
        if (n == 0) return 0;

        this->prices_list = prices;
        
        // dp[i][0] -> selling state at index i
        // dp[i][1] -> buying state at index i
        // Initialize the table with -1 to represent uncached states
        dp.assign(n, std::vector<int>(2, -1));

        // Start at day 0, in 'buying' mode (1)
        return dfs(0, 1);
    }

private:
    int dfs(int i, int buying) {
        // Base case: if we run out of days, no more profit can be made
        if (i >= prices_list.size()) {
            return 0;
        }

        // If the value is already cached, return it directly
        if (dp[i][buying] != -1) {
            return dp[i][buying];
        }

        // Option 1: Choose to do nothing today (Cooldown)
        int cooldown = dfs(i + 1, buying);

        if (buying == 1) {
            // Option 2: Choose to BUY today (transitions state to selling (0) for tomorrow)
            int buy = dfs(i + 1, 0) - prices_list[i];
            dp[i][buying] = std::max(buy, cooldown);
        } else {
            // Option 2: Choose to SELL today (transitions state to buying (1) with a 1-day cooldown skip -> i + 2)
            int sell = dfs(i + 2, 1) + prices_list[i];
            dp[i][buying] = std::max(sell, cooldown);
        }

        return dp[i][buying];
    }
};