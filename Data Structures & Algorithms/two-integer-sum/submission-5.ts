class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const seen = new Map<number, number>();

        for (let i = 0; i<nums.length; i++) {
            const currentNum = nums[i];
            const complement = target - currentNum;

            if (seen.has(complement)) {
                return [seen.get(complement)!, i];
            
            }
            seen.set(currentNum, i);
        }
        return [];
        
    }
}
