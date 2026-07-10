class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        q = []
        n = len(nums)

        for i in range(0,n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] +nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-3] +nums[n-2] + nums[n-1] < target:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + nums[j+1] +nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-1] +nums[n-2] < target:
                    continue
                l = j + 1
                r = n - 1

                while l < r:
                    current_sum = nums[i] + nums[j] + nums[l] + nums[r]

                    if current_sum == target:
                        q.append([nums[i], nums[j], nums[l], nums[r]])

                        while l<r and nums[l] == nums[l+1]:
                            l+=1
                        while l < r and nums[r] == nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
                    elif current_sum < target:
                        l+=1
                    else:
                        r-=1
        return q
        