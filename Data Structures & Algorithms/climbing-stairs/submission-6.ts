class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n: number): number {
        if (n<= 2) return n;

        let first: number = 1;
        let second: number = 2;

        for (let i = 3; i<= n; i++) {
            const third: number = first + second 
            first = second;
            second = third;
        }
        return second;
    }
}
