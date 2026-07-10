#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::vector<std::vector<int>> result;
        int n = nums.size();

        std::sort(nums.begin(), nums.end());

        for (int i = 0; i <n -2; ++i) {

            if (nums[i] > 0) {
                break;
            }

            if (i>0 && nums[i] == nums[i-1]) {
                continue;
            }

            int l = i+1;
            int r = n-1;

            while (l<r) {
                int current_sum = nums[i] + nums[l] + nums[r];

                if (current_sum == 0) {
                    result.push_back({nums[i], nums[l], nums[r]});

                    while (l<r && nums[r] == nums[l+1]) {
                        l++;
                    }
                    while (l < r && nums[r] == nums[r-1]) {
                        r--;
                    }

                    l++;
                    r--;
                }
                else if (current_sum < 0) {
                    l++;
                }
                else {
                    r--;
                }

            }
        }
        return result;
        
    }
};
