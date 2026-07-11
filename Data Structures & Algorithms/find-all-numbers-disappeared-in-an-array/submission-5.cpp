#include <vector>
#include <cmath>

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();

        std::vector<int> res;

        for (int i =1; i <= n; ++i) {

            if (std::find(nums.begin(), nums.end(), i) == nums.end()) {
                res.push_back(i);
            }
        }
        return res;
    }
};