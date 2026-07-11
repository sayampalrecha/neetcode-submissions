#include <vector>
#include <cmath>

class Solution {
public:
    std::vector<int> findDisappearedNumbers(std::vector<int>& nums) {
        std::vector<int> result;
        
        // Step 1: Iterate through the array and mark visited numbers
        for (int i = 0; i < nums.size(); ++i) {
            // Get the target index corresponding to the current number
            int index = std::abs(nums[i]) - 1;
            
            // If the value at that index is positive, flip it to negative
            if (nums[index] > 0) {
                nums[index] = -nums[index];
            }
        }
        
        // Step 2: Look for indices that still contain positive numbers
        for (int i = 0; i < nums.size(); ++i) {
            // If the number is positive, then (i + 1) never appeared in the array
            if (nums[i] > 0) {
                result.push_back(i + 1);
            }
        }
        
        return result;
    }
};