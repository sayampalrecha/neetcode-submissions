class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we need to find i,j,k
        # re-write it as j + k = -i
        nums = sorted(nums)
        t = []
        n = len(nums)

        for i in range(0,n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] >0:
                break
            
            l = i + 1
            r = n - 1

            while l<r:
                current_sum = nums[i] + nums[l] + nums[r]

                if current_sum == 0:
                    t.append([nums[i],nums[l], nums[r]])

                    while l < r and nums[l] == nums[l +1]:
                        l +=1
                    while l <r and nums[r] == nums[r-1]:
                        r -=1
                    
                    l += 1
                    r -= 1
                elif current_sum < 0:
                    l+=1
                else:
                    r-=1
        return t