class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n-1
        max_area = 0

        while i<j:
            w = j - i
            h = min(heights[i],heights[j])
            a = w*h
            max_area = max(max_area, a)
            
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_area
            
            
            
            
        
            

        