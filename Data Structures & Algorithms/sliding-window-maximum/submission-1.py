class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        if n == 0:
            return []
        for i in range(0,n-k+1):
            window = nums[i:k+i]
            max_win = max(window)
            res.append(max_win)
        return res

        