class Solution {
    /**
     * @param {number[]} coins
     * @param {number} amount
     * @return {number}
     */
    
    coinChange(coins: number[], amount: number): number {
    // Fill the array with amount + 1 as our "Infinity" placeholder
    const dp: number[] = new Array(amount + 1).fill(amount + 1);
    
    // Base case: 0 coins are needed to make an amount of 0
    dp[0] = 0;
    
    // Compute the minimum coins for every sub-amount from 1 up to 'amount'
    for (let i = 1; i <= amount; i++) {
        for (const coin of coins) {
            // Only consider the coin if it isn't larger than the sub-amount
            if (i - coin >= 0) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    
    // If dp[amount] is still our placeholder, it means the amount cannot be reached
    return dp[amount] > amount ? -1 : dp[amount];
}
}
